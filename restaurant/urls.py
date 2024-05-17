
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
        path('restaurant/', views.index),
        path('menu/', views.MenuItemsView.as_view()),
        path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
        path('message/', views.msg),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.authtoken')),
        path('api-token-auth/', obtain_auth_token),


]
