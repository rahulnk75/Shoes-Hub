from django.shortcuts import render,redirect
from Shoes_App.models import Category_Db,Product_Db
from Web_App.models import Contact_Db,Register_Db,Cart_Db,Order_Db
from django.contrib import messages
import razorpay

# Create your views here.
def Home_Page(request):
    cat=Category_Db.objects.all()
    pro=Product_Db.objects.all()
    return render(request,'home_page.html',{'cat':cat,'pro':pro})

def Product_Page(request):
    pro=Product_Db.objects.all()
    return render(request,'product_page.html',{'pro':pro})

def contact_page(request):
    return render(request,'contact_page.html')

def save_contact_page(request):
    if request.method == 'POST':
        _first_name=request.POST.get('first_name_')
        _last_name=request.POST.get('last_name_')
        _number=request.POST.get('number_')
        _email=request.POST.get('email_')
        _message=request.POST.get('message_')
        obj=Contact_Db(First_Name=_first_name,Last_Name=_last_name,Phone_Number=_number,Email=_email,Message=_message)
        obj.save()
        messages.success(request,"Send Message")
        return redirect(contact_page)

def About_Page(request):
    return render(request,'about_page.html')

def Product_Filtered(request,cat_name):
    pro_f=Product_Db.objects.filter(Shoes_Category=cat_name)
    return render(request,'product_filtered.html',{'pro_f':pro_f})

def Single_Product(request, sin_id):
    sin=Product_Db.objects.get(id=sin_id)
    return render(request,'single_product.html',{'sin':sin})


def Sign_up(request):
    return render(request,'sing_up.html')

def Save_Sign_up(request):
    if request.method=='POST':
        _username=request.POST.get('username_')
        _p_number=request.POST.get('p_number_')
        _email=request.POST.get('email_')
        _password=request.POST.get('password_')
        _c_password=request.POST.get('c_password_')
        obj=Register_Db(Username=_username,Phone_Number=_p_number,Email=_email,Password=_password,Confirm_password=_c_password)
        obj.save()
        messages.success(request,"Sing Up successfully..!!!")
        return redirect(Sign_up)
    
def Sign_in(request):
    return render(request,'sing_in.html')

def Save_Sign_in(request):
     if request.method=='POST':
        _Username=request.POST.get('Username_')
        _Password=request.POST.get('Password_')
        if Register_Db.objects.filter(Username=_Username,Password=_Password).exists():
            request.session['Username']=_Username
            request.session['Password']=_Password
            messages.success(request,"SignIn successfully..!!!")
            return redirect(Home_Page)
        else:
            messages.info(request,"invalid user..!!!")
            return redirect(Sign_in)
     else:
          messages.info(request,"invalid Password..!!!")
          return redirect(Sign_in)
     
def User_Sign_out(request):
    del request.session['Username']
    del request.session['Password']
    messages.error(request,"Signout Successfully..!!!")
    return redirect(Home_Page)

def Save_Cart(request):
    if request.method=='POST':
        _user_name=request.POST.get('user_name_')
        _product_name=request.POST.get('product_name_')
        _total=request.POST.get('total_')
        _price=request.POST.get('price_')
        _quantity=request.POST.get('quantity_')
        obj=Cart_Db(User_name=_user_name,Product_name=_product_name,Quantity=_quantity,Price=_price,Total_Price=_total)
        obj.save()
        messages.success(request,"Item added to Cart..!!!")
        return redirect(Cart_Page)
def Cart_Page(request):
    Cart=Cart_Db.objects.filter(User_name=request.session['Username'])
    Sub_total=0
    Shipping_amount=0
    total_amount=0
    for i in Cart:
        Sub_total = Sub_total+i.Total_Price
        if Sub_total > 3000:
            Shipping_amount = 100
        else:
            Shipping_amount = 250
        total_amount = Shipping_amount + Sub_total
    return render(request,'cart_page.html',{'Cart':Cart,'Sub_total':Sub_total,'total_amount':total_amount,'Shipping_amount':Shipping_amount,})

def Cart_Delete(request,del_id):
    remov=Cart_Db.objects.filter(id=del_id)
    remov.delete()
    return redirect(Cart_Page)

def Checkout_Page(request):
    che=Cart_Db.objects.all()
    Sub_total=0
    Shipping_amount=0
    total_amount=0
    for i in che:
        Sub_total = Sub_total+i.Total_Price
        if Sub_total > 3000:
            Shipping_amount = 100
        else:
            Shipping_amount = 250
        total_amount = Shipping_amount + Sub_total
    return render(request,'checkout_page.html',{'che':che,'Sub_total':Sub_total,'total_amount':total_amount,'Shipping_amount':Shipping_amount,})

def Order_Save(request):
    if request.method=='POST':
        name=request.POST.get('name_')
        email=request.POST.get('email_')
        phone=request.POST.get('phone_')
        place=request.POST.get('place_')
        total=request.POST.get('total_')
        address=request.POST.get('address_')
        message=request.POST.get('message_')
        obj=Order_Db(Name=name,Email=email,Phone=phone,Place=place,total=total,Address=address,Message=message)
        obj.save()
        return redirect(Payment_Page)

def Payment_Page(request):
    customer=Order_Db.objects.order_by('-id').first()
    payy=customer.total
    amount=int(payy*100)
    payy_str=str(amount)
    if request.method=="POST":
        order_currency= 'INR'
        client=razorpay.Client(auth=('rzp_test_sXSjc7ZbwI7M3J','JfZlKEyC2d0YJZDzcHX4eMjP'))
        payment = client.order.create({'amount':amount,'order_currency':order_currency})

    return render(request,'payment_page.html',{'customer':customer,'payy_str':payy_str})
