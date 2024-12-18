from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart_,name='cart'),
    path('knowus',views.knowus,name='knowus'),
    path('support',views.support,name='support'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('profile_',views.profile,name='profile'),
    path('edit_profile/<int:id>',views.e_p,name='e_p'),
    path('delete_p/<int:id>',views.delete_p,name='delete_p'),
    path('checkout',views.checkout_,name='checkout_'),
    path('increase_quantity/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('order',views.order,name='order'),
    path('trace_order',views.trace_o,name='trace_o'),
]
