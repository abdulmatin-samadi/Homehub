from django.apps import AppConfig


class PagesConfig(AppConfig):
    """Statik/umumiy sahifalar (bosh sahifa va h.k.) uchun ilova."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    verbose_name = 'Sahifalar'
