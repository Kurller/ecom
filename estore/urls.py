from django.urls import path
from estore import views
from .views import home_view,login_view
#app_name = 'estore'

urlpatterns = [
     path('', home_view, name='home'),
    path('<int:id>/', views.productDetail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
     path("register", views.register, name="register"),
   path('login/', login_view, name='login'),
  path('logout/', views.custom_logout, name='logout'),
]