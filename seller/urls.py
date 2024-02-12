from django.urls import path
from.import views
app_name='seller'
urlpatterns=[
    path('sellerhome',views.SellerHome,name='sellerhome'),
    path('signup',views.Signup,name='signup'),
    path('login',views.login,name='login'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('view',views.view,name='view'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('updatepdt/<int:pid>',views.updatepdt,name='updatepdt'),
    path('deletepdt/<int:pid>',views.deletepdt,name='deletepdt'),
    path('message',views.message,name='message'),
    path('message',views.about,name='about'),
    path('forget',views.about,name='forget')
]