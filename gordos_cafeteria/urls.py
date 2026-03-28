from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from products.views import home

urlpatterns = [
    path('', home, name='home'),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),

    # Login y logout propios
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'), name='logout'),
]