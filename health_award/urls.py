from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from health_award.veiws import landing_page



urlpatterns = [
    path('home/', landing_page.as_view(), name='home_page'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings. STATIC_URL, document_root=settings.STATICFILES_DIRS)
