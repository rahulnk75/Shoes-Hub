from django.urls import path
from . import views
urlpatterns = [
    path('Home_Page/',views.Home_Page,name='Home_Page'),
    path('Product_Page/',views.Product_Page,name='Product_Page'),
    path('contact_page/',views.contact_page,name='contact_page'),
    path('save_contact_page/',views.save_contact_page,name='save_contact_page'),
    path('About_Page/',views.About_Page,name='About_Page'),
    path('Product_Filtered/<cat_name>/',views.Product_Filtered,name='Product_Filtered'),
    path('Single_Product/<int:sin_id>/',views.Single_Product,name='Single_Product'),
    path('',views.Sign_in,name='Sign_in'),
    path('Sign_up/',views.Sign_up,name='Sign_up'),
    path('Save_Sign_up/',views.Save_Sign_up,name='Save_Sign_up'),
    path('Save_Sign_in/',views.Save_Sign_in,name='Save_Sign_in'),
    path('User_Sign_out/',views.User_Sign_out,name='User_Sign_out'),
    path('Save_Cart',views.Save_Cart,name='Save_Cart'),
    path('Cart_Page/',views.Cart_Page,name='Cart_Page'),
    path('Cart_Delete/<int:del_id>/',views.Cart_Delete,name='Cart_Delete'),
    path('Checkout_Page/',views.Checkout_Page,name='Checkout_Page'),
    path('Order_Save/',views.Order_Save,name='Order_Save'),
    path('Payment_Page/',views.Payment_Page,name='Payment_Page')
]