from django.urls import path
from .views import upload_and_scan_image

urlpatterns = [
    path('', upload_and_scan_image, name='upload_and_scan_image'),
]