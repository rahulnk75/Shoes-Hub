from django.urls import path
from . import views

urlpatterns = [
    # main_backend
    path('Shoes_Details/',views.Shoes_Details,name='Shoes_Details'),

    # Category_section
    path('Add_Category/',views.Add_Category,name='Add_Category'),
    path('Save_Category/',views.Save_Category,name='Save_Category'),
    path('Display_Category/',views.Display_Category,name='Display_Category'),
    path('Delete_Category/<int:del_id>/',views.Delete_Category,name='Delete_Category'),
    path('Edit_Category/<int:edit_id>/',views.Edit_Category,name='Edit_Category'),
    path('Upload_Category/<int:upd_id>/',views.Upload_Category,name='Upload_Category'),

    # Product_section
    path('Add_Product',views.Add_Product,name='Add_Product'),
    path('Save_Product/',views.Save_Product,name='Save_Product'),
    path('Display_Product/',views.Display_Product,name='Display_Product'),
    path('Delete_Product/<int:del_id>/',views.Delete_Product,name='Delete_Product'),
    path('Edit_Product/<int:edit_id>/',views.Edit_Product,name='Edit_Product'),
    path('Upload_product/<int:upd_id>/',views.Upload_product,name='Upload_product'),
    
    # Admin_section
    path('Login_Page/',views.Login_Page,name='Login_Page'),
    path('Admin_login/',views.Admin_login,name='Admin_login'),
    path('Admin_Logout/',views.Admin_Logout,name='Admin_Logout'),

    # Contact display
    path('Contact_display/',views.Contact_display,name='Contact_display'),
    path('Contact_delete/<int:del_id>/',views.Contact_delete,name='Contact_delete')
]