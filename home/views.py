from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Product, Cart
from customer.models import Contact
from django.contrib import messages
def home(request):
    dishwasher = Product.objects.all().filter(category='dishwasher')[:8]
    lightning = Product.objects.all().filter(category='lightning')[:8]
    mattress = Product.objects.all().filter(category='mattress')[:8]
    carts = Cart.objects.filter(user=request.user.id)
    topRated = Product.objects.all()[1:2:3]
    context = {'dishwasher':dishwasher,
               'mattress':mattress,
               'lightning':lightning,
               'topRated':topRated,
               'carts':len(carts)
               
               }
    
    return render(request, "index.html", context)

def contact(request):
    if request.method == 'POST':
       name =  request.POST['name']
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']
       contact = Contact(name=name, email=email, subject=subject, message=message)
       data = contact.save()
       messages.success(request,'your form is submitted')
       return render(request, "index.html")
       if not data:
           context = {'name':name, 'email':email, 'subject':subject, 'message':message}
           messages.success(request, 'your form is not submitted')
           return render(request, "contact.html", context)
    else:
        return render(request, "contact.html")
       
  

           

def cart(request, id): 
    try:
        if request.user.is_authenticated:
             product = Product.objects.get(id=id)
             if not Cart.objects.filter(product=product).exists():
                 prodt = Cart(product=product, user=request.user, status='pending', is_owned=False)
                 prodt.save()
                 carts = Cart.objects.filter(user=request.user.id)
                 messages.success(request, 'your product is added to your cart, we will contact you')
                 return render(request, 'dashboard.html', {'carts':carts} )
             else:
                 messages.error(request, 'You have this product in your cart')
                 return redirect('home')
        elif not request.user.is_authenticated:
                 messages.error(request, 'Please login to add product to cart')
                 return redirect('home')   
    except ValueError as identifier:
             return redirect('home')
        

def about(request):
    return render(request, "about-us.html")


def search(request):
    queryset_list = Product.objects.order_by('date')
    product = Product.objects.all()
    data = request.GET['keywords']
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(details__icontains=keywords) | Q(name__icontains=keywords)| Q(category__icontains=keywords))
            if queryset_list:
                return render(request, 'search.html', {'search':queryset_list})
            else: 
                return render(request, 'search.html', {'search':product, 'error':f'No match found "{data}" try keysword(vault, mattress, dishwasher...)', 'data':data})
    else:
        return render(request, 'search.html', {'search':product})

def product(request, id):
    product = Product.objects.get(id=id)
    category = Product.objects.all().filter(category=product.category)
    context = {
        'product':product,
        'category':category
    }
    
    return render(request, 'product-details-affiliate.html', context)

def delivery(request):
    return render(request, 'delivery.html')

def terms(request):
    return render(request, 'terms.html')

def policy(request):
    return render(request, 'policy.html')

def vault(request):
    vault = Product.objects.all().filter(category='vault')
    return render(request, 'vault.html', {'vault':vault})

def lightning(request):
    lightning = Product.objects.all().filter(category='lightning')
    return render(request, 'lightning.html', {'lightning':lightning})


def bateriesandpanels(request):
    bateriesandpanels = Product.objects.all().filter(category='bateriesandpanels')
    return render(request, 'bateriesandpanels.html', {'bateriesandpanels':bateriesandpanels})

def mattress(request):
    mattress = Product.objects.all().filter(category='mattress')
    return render(request, 'mattress.html', {'mattress':mattress})

def bequipment(request):
    bequipment = Product.objects.all().filter(category='bequipment')
    return render(request, 'bequipment.html', {'bequipment':bequipment})

def dishwasher(request):
    dishwasher = Product.objects.all().filter(category='dishwasher')
    return render(request, 'dishwasher.html', {'dishwasher':dishwasher})
