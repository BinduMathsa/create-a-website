from django.urls import path
from . import views

urlpatterns=[

    path('',views.myfunctioncall,name='index'),
    path('about',views.myfunctionabout,name='about'),
    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('register',views.register,name='register'),
    path('sign',views.sign,name='sign'),
    path('abou',views.abou,name='adou'),
    path('instruct',views.instruct,name='instruct'),
    path('view',views.view,name='view'),
    path('python',views.python,name='python'),
    path('django',views.django,name='django'),
    path('java',views.java,name='java'),
    path('net',views.net,name='net'),
    path('ps',views.ps,name='ps'),
    path('contact',views.contact,name='contact'),
    
]
