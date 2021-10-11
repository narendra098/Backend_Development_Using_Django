from django.shortcuts import render
from .models import shoes
# Create your views here.
def index(request):
    shoe = shoes.objects.all()
    return render(request,'index.html',{'shoe':shoe})