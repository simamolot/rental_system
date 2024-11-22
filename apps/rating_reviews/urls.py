from django.urls import path

from apps.rating_reviews.views.review_create import ReviewList

urlpatterns = [
    path('create_review/<int:pk>/', ReviewList.as_view(), name='create_review'),

]