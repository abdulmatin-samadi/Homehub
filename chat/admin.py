from django.contrib import admin
from .models import Conversation, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('sender', 'text', 'created_at', 'is_read')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('listing', 'buyer', 'seller', 'created_at')
    search_fields = ('listing__title', 'buyer__username', 'seller__username')
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
