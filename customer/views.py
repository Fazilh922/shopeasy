from django.shortcuts import render,redirect
from seller.models import *
from.models import *
# Create your views here.
def indexhome(request):
    if 'customer' in request.session:
        return render(request,'customer/home.html')
    else:
        return render(request,'customer/firstpage.html')
def Login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            cust=Customer.objects.get(email=email,password=password)
            request.session['customer']=cust.id
            return redirect('customer:home')
        except Customer.DoesNotExist:
            return render(request,'customer/loginpage.html')
    return render(request,'customer/loginpage.html')
def Signup(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        PhoneNumber=request.POST['phone']
        password=request.POST['password']
        cust=Customer(name=name,number=PhoneNumber,email=email,password=password)
        cust.save()
        return redirect('customer:login')
    return render(request,'customer/signuppage.html')
def Accessories(request):
    cat=Category.objects.get(name='Accessories')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/accessories.html',{'product':ph})
    
def homeapplyance(request):
    cat=Category.objects.get(name='Home Applyances')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/homeapplyance.html',{'product':ph})
   
def smartphones(request):
    cat=Category.objects.get(name='phone')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/smartphones.html',{'product':ph})
def watches(request):
    cat=Category.objects.get(name='Watches')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/watches.html',{'product':ph})
   
def gaming(request):
    cat=Category.objects.get(name='Gaming Accessories')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/gaming.html',{'product':ph})
    
def laptops(request):
    cat=Category.objects.get(name='laptop')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/laptops.html',{'product':ph})
    
def formalmens(request):
    cat=Category.objects.get(name='Mens')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/formalmens.html',{'product':ph})
    
def toptrends(request):
    cat=Category.objects.get(name='Trend')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/toptrends.html',{'product':ph})
  
def womens(request):
    cat=Category.objects.get(name='Womensfashion')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/Womens.html',{'product':ph})
    
def bride(request):
    cat=Category.objects.get(name='Bridal')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/bride.html',{'product':ph})
  
def classictrends(request):
    cat=Category.objects.get(name='Boys')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/classictrends.html',{'product':ph})

def kids(request):
    cat=Category.objects.get(name='Girls')
    ph=Product.objects.filter(category=cat)
    return render(request,'customer/kids.html',{'product':ph})
  
def firstpage(request):
    return render(request,'customer/firstpage.html')
def about(request):
    return render(request,'customer/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        text=request.POST['msg']
        cust=Messages(name=name,number=number,email=email,text=text)
        cust.save()
        return render(request,'customer/home.html',{'msg':'message sent succu'})
    return render(request,'customer/contact.html')

   
def addcart(request):
    cart_items=Cart.objects.all()
    total_price=sum(item.product.price*item.quantity for item in cart_items)
    total_price_per_item=[]
    grand_total=0
    for item in cart_items:
        item_total=item.product.price*item.quantity
        total_price_per_item.append({'item':item,'total':item_total})
        grand_total+=item_total
    return render(request,'customer/addcart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
def add_to_cart(request,product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
    return redirect('customer:addcart')
def remove_from_cart(request,product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item=Cart.objects.get(product=product)
        cart_item.delete()
        return redirect('customer:addcart')
def forget(request):
    return render(request,'customer/forget.html')
def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('customer:firstpage')
def pay(request):
    return render(request,'customer/pay.html')
