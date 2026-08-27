# HomeHub — O'zbekiston uchun Ko'chmas Mulk Platformasi

To'liq Django loyihasi: Authentication, Property CRUD, Search/Filter,
Favorites, Reviews, Chat, Dashboard, Admin panel va REST API.

## O'rnatish

```bash
cd homehub
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

python manage.py makemigrations users properties favorites reviews chat payments
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Brauzerda: **http://127.0.0.1:8000/**

## Ilovalar va URL xaritasi

| App | URL prefiksi | Vazifasi |
|---|---|---|
| `pages` | `/` | Bosh sahifa (Hero, Search, Premium, So'nggi e'lonlar) |
| `users` | `/users/` | Register, Login, Logout, Profile, Avatar, Parol |
| `properties` | `/elonlar/` | E'lonlar ro'yxati, filtr, CRUD, tafsilot |
| `favorites` | `/sevimlilar/` | Sevimlilar ro'yxati, ♥ toggle |
| `reviews` | `/sharhlar/` | Sharh qo'shish (property detail sahifasidan) |
| `chat` | `/xabarlar/` | Suhbatlar ro'yxati va yozishmalar |
| `dashboard` | `/dashboard/` | Shaxsiy boshqaruv paneli |
| `payments` | admin orqali | Premium e'lon uchun to'lov (hozircha admin tasdiqlaydi) |
| `api` | `/api/` | REST API (DRF) — `/api/properties/` |
| Admin | `/admin/` | To'liq boshqaruv paneli |

## Muhim texnik izohlar

- **Custom User modeli** (`users.User`) — `phone_number`, `avatar`, `role`, `bio`.
- **Property** modelida barcha talab qilingan maydonlar bor: sarlavha, tavsif,
  narx, viloyat, tuman, manzil, maydon, xonalar, qavat, qurilgan yil, holati,
  bitim turi, asosiy va qo'shimcha rasmlar, egasi. `latitude`/`longitude`
  ixtiyoriy — kiritilsa, tafsilot sahifasida OpenStreetMap xaritasi chiqadi
  (API kalit talab qilinmaydi).
- **CRUD** to'liq Class-Based View'lar orqali (`ListView`, `DetailView`,
  `CreateView`, `UpdateView`, `DeleteView`) — faqat e'lon egasi tahrirlash/
  o'chirish huquqiga ega (`OwnerRequiredMixin`).
- **Qidiruv/filtr**: `q`, `region`, `deal_type`, `min_price`, `max_price`,
  `rooms`, `min_area`, `max_area` GET-parametrlari orqali (`/elonlar/?region=...`).
- **Chat** — real-time (WebSocket) emas, oddiy sahifa yangilanishi asosida
  ishlaydi. Real-time uchun kelajakda Django Channels qo'shish mumkin.
- **Payments** — hozircha haqiqiy to'lov shlyuzi (Payme/Click) ulanmagan,
  chunki bu API shartnoma/kalit talab qiladi. `Payment` modeli va admin
  paneli orqali premium e'lonni qo'lda tasdiqlash infratuzilmasi tayyor —
  keyinchalik haqiqiy shlyuz osongina ulanadi.
- **REST API** — `djangorestframework` orqali, `/api/properties/` da to'liq
  CRUD, faqat egasi o'zgartira oladi (`IsOwnerOrReadOnly`).
- Sayt to'liq **o'zbek tilida**, dizayn Airbnb/Zillow/OLX uslubida,
  responsive, rounded-card, hover-animatsiyali. Dark Mode uchun
  `static/css/style.css` dagi CSS o'zgaruvchilari (`--bg-body`, `--text-body`)
  tayyor.

## Tekshirish tartibi

1. Ro'yxatdan o'ting → profilga avatar yuklang
2. Yangi e'lon qo'shing (asosiy + qo'shimcha rasmlar, ixtiyoriy koordinata)
3. Bosh sahifada va `/elonlar/` da ko'rinishini tekshiring
4. Filtrlarni sinab ko'ring
5. Boshqa hisob bilan kirib, ♥ bosing, sharh qoldiring, "Bog'lanish" orqali
   xabar yozing
6. `/dashboard/` da hammasi jamlanganini ko'ring
7. `/admin/` orqali foydalanuvchilar, e'lonlar, sharhlar, chatlarni boshqaring
# Homehub
