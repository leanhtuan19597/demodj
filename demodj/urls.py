
from django.contrib import admin
from django.urls import path, include

# đây là đường dẫn urls
urlpatterns = [
    path('', include('home.urls')),
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
]
