from django.urls import path
from resize.views import ResizeImagesView


urlpatterns = [
    path('images-to-resize/', ResizeImagesView.as_view()),
    path('search-image/<int:user_id>/', ResizeImagesView.as_view()),
]