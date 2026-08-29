"""HomeHub loyihasi uchun WSGI konfiguratsiyasi (production server uchun)."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homehub.settings')
application = get_wsgi_application()
