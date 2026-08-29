"""
Property (e'lon) uchun to'liq CRUD:
List (ro'yxat), Detail (batafsil), Create (qo'shish),
Update (tahrirlash), Delete (o'chirish).

Django Best Practice: CRUD uchun tayyor Generic Class-Based View'lar
ishlatiladi - bu takroriy kodni kamaytiradi va xavfsizlikni oshiradi.
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from favorites.models import Favorite
from pages.constants import UZ_REGIONS
from reviews.forms import ReviewForm
from .forms import PropertyForm, PropertyImageFormSet
from .models import Property


class OwnerRequiredMixin(UserPassesTestMixin):
    """Faqat e'lon egasi tahrirlash/o'chirish huquqiga ega bo'lishini ta'minlaydi."""

    def test_func(self):
        property_obj = self.get_object()
        return self.request.user == property_obj.owner

    def handle_no_permission(self):
        messages.error(self.request, "Bu amalni bajarish uchun huquqingiz yo'q.")
        return redirect('properties:property_detail', pk=self.kwargs['pk'])


class PropertyListView(ListView):
    """
    Barcha faol e'lonlar ro'yxati + qidiruv/filtr.
    Qo'llab-quvvatlanadigan GET parametrlari:
    q, region, deal_type, min_price, max_price, rooms, min_area, max_area
    """

    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 12

    def get_queryset(self):
        queryset = Property.objects.filter(is_active=True).select_related('owner')
        params = self.request.GET

        q = params.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(description__icontains=q) | Q(address__icontains=q)
            )

        region = params.get('region')
        if region:
            queryset = queryset.filter(region=region)

        deal_type = params.get('deal_type')
        if deal_type:
            queryset = queryset.filter(deal_type=deal_type)

        min_price = params.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        max_price = params.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        rooms = params.get('rooms')
        if rooms:
            queryset = queryset.filter(rooms__gte=rooms)

        min_area = params.get('min_area')
        if min_area:
            queryset = queryset.filter(area__gte=min_area)

        max_area = params.get('max_area')
        if max_area:
            queryset = queryset.filter(area__lte=max_area)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = UZ_REGIONS
        context['request_get'] = self.request.GET
        if self.request.user.is_authenticated:
            context['favorited_ids'] = set(
                Favorite.objects.filter(user=self.request.user).values_list('property_id', flat=True)
            )
        else:
            context['favorited_ids'] = set()
        return context


class PropertyDetailView(DetailView):
    """Bitta e'lonning to'liq tafsilotlari: rasmlar, sharhlar, sevimli holati."""

    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'

    def get_queryset(self):
        return Property.objects.select_related('owner').prefetch_related('images', 'reviews__user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property_obj = self.object

        context['reviews'] = property_obj.reviews.select_related('user')
        context['average_rating'] = property_obj.reviews.aggregate(avg=Avg('rating'))['avg']
        context['review_form'] = ReviewForm()

        user = self.request.user
        context['is_favorited'] = (
            user.is_authenticated and Favorite.objects.filter(user=user, property=property_obj).exists()
        )
        context['user_has_reviewed'] = (
            user.is_authenticated and property_obj.reviews.filter(user=user).exists()
        )
        return context


class PropertyCreateView(LoginRequiredMixin, CreateView):
    """Yangi e'lon qo'shish. Faqat tizimga kirgan foydalanuvchilar uchun."""

    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_formset'] = PropertyImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['image_formset'] = PropertyImageFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        image_formset = context['image_formset']

        response = super().form_valid(form)  # self.object shu yerda o'rnatiladi

        if image_formset.is_valid():
            image_formset.instance = self.object
            image_formset.save()

        messages.success(self.request, "E'lon muvaffaqiyatli qo'shildi.")
        return response


class PropertyUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    """Mavjud e'lonni tahrirlash. Faqat egasi tahrirlay oladi."""

    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_formset'] = PropertyImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['image_formset'] = PropertyImageFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']

        response = super().form_valid(form)

        if image_formset.is_valid():
            image_formset.instance = self.object
            image_formset.save()

        messages.success(self.request, "E'lon muvaffaqiyatli yangilandi.")
        return response


class PropertyDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    """E'lonni o'chirish. Faqat egasi o'chira oladi."""

    model = Property
    template_name = 'properties/property_confirm_delete.html'
    success_url = reverse_lazy('properties:property_list')

    def form_valid(self, form):
        messages.success(self.request, "E'lon o'chirildi.")
        return super().form_valid(form)
