from django.shortcuts import render,redirect
from . models import *
from customer.models import *

# Create your views here.
# def signup(request):

#     if request.method=='post':
#         name=request.POST['name']
#         email=request.POST['email']
#         number=request.POST['number']
#         password=request.POST['password']
#         confirmpassword=request.POST['confirmpassword']
#         seller=Seller(name=name,email=email,number=number,password=password,confirmpassword=confirmpassword)
#         seller.save()
#     return render(request,'seller/signup.html')    
def SellerHome(request):
    return render(request,'seller/sellerhome.html')
def Signup(request):
    if request.method=='POST':
        name=request.POST['firstname']
        name=request.POST['lastname']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        seller=Seller(firstname=name,lastname=name,number=number,password=password)
        seller.save()
    return render(request,'seller/signup.html')
def login(request):
    if request.method=='POST':
        email=request.post['email']
        password=request.POST['password']

       
        try:
            sel=Seller.objects.get(email=email,password=password)
        except Seller.DoesNotExist:
            err='invalid user name or password'
            return render(request,'seller/login.html',{'error':err})
        

    return render(request,'seller/login.html')
def addproduct(request):
    categories=Category.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES['imag']
        stock=request.POST['stock']
        quantity=request.POST['quantity']
        price=request.POST['price']
        category_id=request.POST.get('category')
        category=Category.objects.get(pk=category_id)
        product=Product(product=title,description=description,stock=stock,quantity=quantity,category=category,image=image,price=price)
        product.save()
        return redirect('seller:view')
    return render(request,'seller/addproduct.html',{'categories':categories})
def view(request):
    pdt=Product.objects.all()
    return render(request,'seller/view.html',{'products':pdt})
def dashboard(request):
    return render(request,'seller/dashboard.html')
def updatepdt(request,pid):
    categories=Category.objects.all()
    pdt=Product.objects.get(id=pid)
    if request.method=='POST':
        title=request.POST['product']
        description=request.POST['description']
        price=request.POST['price']
        category_id=request.POST.get('category')
        quantity=request.POST['quantity']
        stock=request.POST['stock']
        category=Category.objects.get(pk=category_id)
        pdt.product=title
        pdt.description=description
        pdt.price=price
        pdt.category=category
        pdt.stock=stock
        pdt.quantity=quantity
        if 'image' in request.FILES:
            image = request.FILES['image']
            pdt.image = image
        else:
            image = pdt.image if pdt.image else None
        pdt.category=category
        pdt.save()
        return redirect('seller:view')


    return render(request,'seller/updatepdt.html',{'product':pdt,'category':categories})

def deletepdt(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('seller:view')
def message(request):
    msg=Messages.objects.all()
    return render(request,'seller/message.html',{'msg':msg})
def about(request):
    return render(request,'seller/about.html')
def forget(request):
    return render(request,'seller/forget.html')


