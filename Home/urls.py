from django.contrib import admin
from django.urls import path
from Home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)