from django.shortcuts import render
from django.views import View
from . models import Product
# Create your views here.


# def home(request):
#     return render(request,'base.html')



class ListView(View):
    def get(self,request):
        products=Product.objects.all()
        context={"product_list":products}
        return render(request,'index.html',context)
