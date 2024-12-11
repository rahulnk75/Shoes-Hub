from django.shortcuts import render,redirect
from Shoes_App.models import Category_Db,Product_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from Web_App.models import Contact_Db
from django.contrib import messages

# Create your views here.
def Shoes_Details(request):
    date=datetime.datetime.now
    c_count=Category_Db.objects.count
    p_count=Product_Db.objects.count
    return render(request,'index.html',{'c_count':c_count,'p_count':p_count,'date':date})
 
# start category section

def Add_Category(request):
    return render(request,'add_category.html')

def Save_Category(request):
    if request.method=='POST':
        _Shoes_Category=request.POST.get('Shoes_Category_')
        _Shoes_Brand=request.POST.get('Shoes_Brand_')
        _Discription=request.POST.get('Description_')
        _Shoes_Images=request.FILES['Shoes_Images_']
        obj=Category_Db(Shoes_Brand=_Shoes_Brand,Shoes_Category=_Shoes_Category,Description=_Discription,Shoes_Images=_Shoes_Images)
        messages.success(request,"Save Category..!!!")
        obj.save()
        return redirect(Add_Category)

def Display_Category(request):
    dis=Category_Db.objects.all()
    return render(request,'display_category.html',{'pass':dis})

def Delete_Category(request,del_id):
    remov=Category_Db.objects.filter(id=del_id)
    remov.delete()
    messages.error(request,"deleted Category..!!")
    return redirect(Display_Category)

def Edit_Category(request,edit_id):
    edit=Category_Db.objects.get(id=edit_id)
    return render(request,'edit_category.html',{'pass':edit})

def Upload_Category(request,upd_id):
     if request.method=='POST':
        _Shoes_Category=request.POST.get('Shoes_Category_')
        _Shoes_Brand=request.POST.get('Shoes_Brand_')
        _Discription=request.POST.get('Description_')
        try:
            _Shoes_Images=request.FILES['Shoes_Images_']
            fs=FileSystemStorage()
            Shoes_Images=fs.save(_Shoes_Images.name,_Shoes_Images)
        except MultiValueDictKeyError:
            Shoes_Images=Category_Db.objects.get(id=upd_id).Shoes_Images

        Category_Db.objects.filter(id=upd_id).update(Shoes_Brand=_Shoes_Brand,Shoes_Category=_Shoes_Category,Description=_Discription,Shoes_Images=Shoes_Images)
        messages.success(request,"Updated successfully..!!!")
        return redirect(Display_Category)
     
# end category section
# start product section     

def Add_Product(request):
    Category_name=Category_Db.objects.all()
    return render(request,'add_product.html',{'key':Category_name})

def Save_Product(request):
    if request.method=='POST':
        _Shoes_Category=request.POST.get('Shoes_Category_')
        _Shoes_Brand=request.POST.get('Shoes_Brand_')
        _Product_Name=request.POST.get('Product_Name_')
        _Quantity=request.POST.get('Quantity_')
        _Country_of_origin=request.POST.get('Country_of_origin_')
        _Manufactured_By=request.POST.get('Manufactured_By_')
        _Description=request.POST.get('Description_')
        _MRP=request.POST.get('MRP_')
        _Size=request.POST.get('Size_')
        _Product_Image_1=request.FILES['Product_Image_1_']
        _Product_Image_2=request.FILES['Product_Image_2_']
        _Product_Image_3=request.FILES['Product_Image_3_']
        _Product_Image_4=request.FILES['Product_Image_4_']
        _Product_Image_5=request.FILES['Product_Image_5_']
        obj=Product_Db(Shoes_Category=_Shoes_Category,Shoes_Brand=_Shoes_Brand,Product_Name=_Product_Name,Quantity=_Quantity,Country_of_origin=_Country_of_origin,Manufactured_By=_Manufactured_By,Description=_Description,MRP=_MRP,Size=_Size,Product_Image_1=_Product_Image_1,Product_Image_2=_Product_Image_2,Product_Image_3=_Product_Image_3,Product_Image_4=_Product_Image_4,Product_Image_5=_Product_Image_5)
        obj.save()
        messages.success(request,"Save Product..!!!")
        return redirect(Add_Product)
    
def Display_Product(request):
    dis=Product_Db.objects.all()
    return render(request,'display_product.html',{'key':dis})

def Delete_Product(request,del_id):
    remov=Product_Db.objects.filter(id=del_id)
    remov.delete()
    messages.error(request,"Delete Product..!!!")
    return redirect(Display_Product)

def Edit_Product(request,edit_id):
    category_name=Category_Db.objects.all()
    edit=Product_Db.objects.get(id=edit_id)
    return render(request,'edit_product.html',{'key':edit,'pass':category_name})

def Upload_product(request,upd_id):
     if request.method=='POST':
        _Shoes_Category=request.POST.get('Shoes_Category_')
        _Shoes_Brand=request.POST.get('Shoes_Brand_')
        _Product_Name=request.POST.get('Product_Name_')
        _Quantity=request.POST.get('Quantity_')
        _Country_of_origin=request.POST.get('Country_of_origin_')
        _Manufactured_By=request.POST.get('Manufactured_By_')
        _Description=request.POST.get('Description_')
        _MRP=request.POST.get('MRP_')
        _Size=request.POST.get('Size_')
        try:
            _Product_Image_1=request.FILES['Product_Image_1_']
            fs=FileSystemStorage()
            product_image_1=fs.save(_Product_Image_1.name,_Product_Image_1)
        except MultiValueDictKeyError:
            product_image_1=Product_Db.objects.get(id=upd_id).Product_Image_1

        try:
            _Product_Image_2=request.FILES['Product_Image_2_']
            fs=FileSystemStorage()
            product_image_2=fs.save(_Product_Image_2.name,_Product_Image_2)
        except MultiValueDictKeyError:
            product_image_2=Product_Db.objects.get(id=upd_id).Product_Image_2

        try:
            _Product_Image_3=request.FILES['Product_Image_3_']
            fs=FileSystemStorage()
            product_image_3=fs.save(_Product_Image_3.name,_Product_Image_3)
        except MultiValueDictKeyError:
            product_image_3=Product_Db.objects.get(id=upd_id).Product_Image_3

        try:
            _Product_Image_4=request.FILES['Product_Image_4_']
            fs=FileSystemStorage()
            product_image_4=fs.save(_Product_Image_4.name,_Product_Image_4)
        except MultiValueDictKeyError:
            product_image_4=Product_Db.objects.get(id=upd_id).Product_Image_4

        try:
            _Product_Image_5=request.FILES['Product_Image_5_']
            fs=FileSystemStorage()
            product_image_5=fs.save(_Product_Image_5.name,_Product_Image_5)
        except MultiValueDictKeyError:
            product_image_5=Product_Db.objects.get(id=upd_id).Product_Image_5

        

        Product_Db.objects.filter(id=upd_id).update(Shoes_Category=_Shoes_Category,Shoes_Brand=_Shoes_Brand,Product_Name=_Product_Name,Quantity=_Quantity,Country_of_origin=_Country_of_origin,Manufactured_By=_Manufactured_By,Description=_Description,MRP=_MRP,Size=_Size,Product_Image_1=product_image_1,Product_Image_2=product_image_2,Product_Image_3=product_image_3,Product_Image_4=product_image_4,Product_Image_5=product_image_5)
        messages.success(request,"Updated successfully..!!!")
        return redirect(Display_Product)
# end product section 
# start admin section

def Login_Page(request):
    return render(request,'admin_login.html')

def Admin_login(request):
    if request.method=='POST':
        _Username=request.POST.get('Username_')
        _Password=request.POST.get('Password_')
        if User.objects.filter(username__contains=_Username).exists():
            _user=authenticate(username=_Username,password=_Password)
            if _user is not None:
                login(request,_user)
                request.session['username']=_Username
                request.session['password']=_Password
                messages.success(request,"Login successfully...!!!")
                return redirect(Shoes_Details)
            else:
                messages.info(request,"Invalid Password...!!!")
                return redirect(Login_Page)
        else:
            messages.error(request,"Invalid User..!!!")
            return redirect(Login_Page)
def Admin_Logout(request):
    del  request.session['username']
    del  request.session['password']
    messages.error(request,"Logout Successfully..!!!")
    return redirect(Login_Page)

# end admin section
# contact page display

def Contact_display(request):
    obj=Contact_Db.objects.all()
    return render(request,'display_contact_page.html',{'obj':obj})

def Contact_delete(request,del_id):
    remov=Contact_Db.objects.filter(id=del_id)
    remov.delete()
    messages.error(request,"Message Deleted..!!!")
    return redirect(Contact_display)



