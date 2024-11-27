
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

    path('cart/',views.show_cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('orders/remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout',views.checkout_cart,name='checkout'),
    path('orders',views.show_orders,name='orders')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






