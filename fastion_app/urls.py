from django.urls import path
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('onepiece/', views.onepiece, name='onepiece'),
    path('salwarkameez/', views.salwarkameez, name='salwarkameez'),
    path('saree/', views.saree, name='saree'),
    path('babyboy/', views.babyboy, name='babyboy'),
    path('babygirl/', views.babygirl, name='babygirl'),
    path('accessories/', views.accessories, name='accessories'),
    path('groom/', views.groom, name='groom'),
    path('bride/', views.bride, name='bride'),
    path('shoes/', views.shoes, name='shoes'),
    path('bag/', views.bag, name='bag'),
    path('men1/', views.men1, name='men1'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('sale/', views.sale, name='sale'),
    path('terms/', views.terms, name='terms'),
    path('career/', views.career, name='career'),
    path('professionalJobs/', views.professionalJobs, name='professionalJobs'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('cookie/', views.cookie, name='cookie'),
    path('myCart/', views.myCart, name='myCart'),
    path('appointment/', views.appointment, name='appointment'),
    path('professionalIntern/', views.professionalIntern, name='professionalIntern'),
    path('privacy/', views.privacy, name='privacy'),
    path('locations/', views.locations, name='locations'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('license/', views.license, name='license'),
    path('faq/', views.faq, name='faq'),
    path('jobapply/', views.jobapply, name='jobapply'),
    path('code/', views.code, name='code'),
    path('payment/', views.payment_view, name='payment'),
    path('logout/', views.logout_view, name='logout'), 
    path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
     path('payment/', views.payment_view, name='payment'),
    path('payment_done/', views.payment_done, name='payment_done'),
path('accounts/login/', views.login, name='login'),

    
]   

