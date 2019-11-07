from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#set up the urls for all associated apps within the project
urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('jobs/', include('jobs.urls')),
    path('donations/', include('donations.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
