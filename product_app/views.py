from django.shortcuts import render,redirect
from django.views.generic import View
from product_app.models import Productmodel
from product_app.forms import ProductForm
from product_app.models import Cartmodel
# from django.shortcuts import get_object_or_404

# Create your views here.
class Createproduct(View):
    def get(self,request):
        form = ProductForm()
        return render(request,"product_add.html",{"form":form})
    
    def post(self,request):
        print(request.POST)
        name = request.POST.get('name')

        price = request.POST.get('price')

        stock = request.POST.get('stock')

        Productmodel.objects.create(name = name,price = price,stock = stock)

        form = ProductForm
        return redirect("product_list")
        # return render(request,"product_add.html",{"form":form})

class Listproduct(View):
    def get(self,request):
        data = Productmodel.objects.all()
        return render(request,"product_list.html",{"data":data})
    
class Updateproduct(View):
   def get(self,request,**kwargs):
       update_id =kwargs.get("pk")
       product = Productmodel.objects.get(id=update_id)
       form=ProductForm(instance=product)
       return render(request,"product_update.html",{"form":form})
   
   def post(self,request,**kwargs):
        update_id=kwargs.get("pk")
        product = Productmodel.objects.get(id=update_id)
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        return render(request,"product_update.html")
   
class Deleteproduct(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        product = Productmodel.objects.get(id=id)
        product.delete()
        return redirect("product_list")
        # return render(request,"product_list.html")

class Cartaddview(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        product = Productmodel.objects.get(id=id)
        Cartmodel.objects.create(product=product,quantity =1)
        return render(request,"product_list.html")
       

    