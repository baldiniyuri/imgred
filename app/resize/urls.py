from django.urls import path
from resize.views import ResizeImagesView


urlpatterns = [
    path('images-to-resize/', ResizeImagesView.as_view()),
    path('logs/', ResizeImagesView.as_view()),
]