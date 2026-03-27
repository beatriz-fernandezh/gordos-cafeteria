from django.contrib import admin
from django.urls import path, include
from products.views import home

urlpatterns = [
    path('', home, name='home'),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]