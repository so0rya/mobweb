from mobiles import views
from django.urls import path, include


urlpatterns = [
    path('add-mobile', views.MobileCreateView.as_view(),name='add-mobile')
]
