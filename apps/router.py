from django.urls import path, include

urlpatterns = [
    path('apartments/', include('apps.apartments.urls')),
    path('user/', include('apps.user.urls')),
    path('reservations/', include('apps.reservations.urls')),
    path('reviews/', include('apps.rating_reviews.urls'))
]