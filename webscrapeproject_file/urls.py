from django.urls import path
from . import views
urlpatterns= [

    path('home/',views.home,name='home'),
    path('home/itjob/',views.itjob,name='itjob'),
    path('home/hotwheels/',views.hotwheels,name='hotwheels'),
    path('home/goldprice/',views.goldprice,name='goldprice')
]