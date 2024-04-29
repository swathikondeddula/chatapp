# urls.py in wechatpp project

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importing auth views for logout
from chatapp import views
from django.conf import settings
from django.conf.urls.static import static  # Importing views from chatapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # Including auth URLs
    path('', include('chatapp.urls')),  # Including chatapp URLs
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)