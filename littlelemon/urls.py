"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from inventory import views as inventory_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'tables', views.BookingViewSet)
menuitemrouter = routers.SimpleRouter()
menuitemrouter.register(r'items', views.MenuItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu-items/', include(menuitemrouter.urls)),
    path('restaurant/menu/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('booking/', include(router.urls)),
    path('message/', views.msg),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    path('restaurant/about/', views.about, name='about'),
    path('restaurant/bookTable', views.book_table, name="book_table"),
    path('restaurant/loginUser', views.login_user, name="login_user"),
    path('restaurant/newUser', views.sign_up_user, name="sign_up_user"),
    path('inventory/admin/', inventory_views.inventory, name="inventory"),
    path('inventory/adminLogin/', inventory_views.login_user, name="inventoryLogin")

]
