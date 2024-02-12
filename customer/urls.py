from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('home/',views.indexhome,name="home"),
    path('login/',views.Login,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('accessories/',views.Accessories,name='accessories'),
    path('homeapplyance/',views.homeapplyance,name='homeapplyance'),
    path('smartphones/',views.smartphones,name='smartphones'),
    path('watches/',views.watches,name='watches'),
    path('gaming/',views.gaming,name='gaming'),
    path('laptops/',views.laptops,name='laptops'),
    path('formalmens/',views.formalmens,name='formalmens'),
    path('toptrends/',views.toptrends,name='toptrends'),
    path('womens/',views.womens,name='womens'),
    path('bride/',views.bride,name='bride'),
    path('classictrends/',views.classictrends,name='classictrends'),
    path('kids/',views.kids,name='kids'),
    path('',views.firstpage,name='firstpage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('addcart/',views.addcart,name='addcart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('forget/',views.forget,name='forget'),
    path('logout/',views.logout,name='logout'),
    path('pay/',views.pay,name='pay')





]