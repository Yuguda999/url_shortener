from django.urls import path
from .views import CreateShortURL, RetrieveOriginalURL, UpdateShortURL, DeleteShortURL, URLStats

urlpatterns = [
    path('shorten/', CreateShortURL.as_view(), name='create_short_url'),
    path('shorten/<str:short_code>/', RetrieveOriginalURL.as_view(), name='retrieve_original_url'),
    path('shorten/<str:short_code>/update/', UpdateShortURL.as_view(), name='update_short_url'),
    path('shorten/<str:short_code>/delete/', DeleteShortURL.as_view(), name='delete_short_url'),
    path('shorten/<str:short_code>/stats/', URLStats.as_view(), name='url_stats'),
]
