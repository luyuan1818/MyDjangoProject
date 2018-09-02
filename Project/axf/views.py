from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    return render(request,'axf/home.html',{"title":"主页","wheels":wheels
                                           ,"navs":navs})

def market(request):
    return render(request,'axf/market.html')
def cart(request):
    return render(request,'axf/cart.html')
def mine(request):
    return render(request,'axf/mine.html')
# def home(request):
#     return render(request,'axf/home.html')