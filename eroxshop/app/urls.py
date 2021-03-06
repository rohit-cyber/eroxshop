from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('', views.ProductView.as_view(),name='product'),

    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),

     path('mobile/', views.mobile, name='mobile'),
     path('mobile/<str:data>',views.mobile, name='mobiledata'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.CustomerProfile.as_view(),name='customerprofile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
   
    path('login/', views.Login.as_view(), name='login'),
    path('logout',views.logout, name='logout'),
    path('registration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
