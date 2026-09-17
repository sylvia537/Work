from django.urls import path 
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main, name='main'),
    path('more/', views.more, name='more'),
    path('page/<int:pk>/', views.page, name='page'),
    path('cart/', views.cart, name='cart'),
    path('explore/', views.explore, name='explore'),
]