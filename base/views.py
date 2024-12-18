from django.shortcuts import render ,HttpResponse ,redirect
from .models import Product 
from .models import cart
from  base.models import checkout,Order
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ch_form
from django.core.paginator import Paginator

def home(request):
    categories=Product.objects.all()
    categories_list=[]
    not_match=False
    for i in categories:
        print(i.category)
        if i.category not in categories_list:
            categories_list+=[i.category]
        print(categories_list)



    
    if request.user.is_authenticated:
        count_=cart.objects.filter(host=request.user).count()
        print(count_)

    else:
        count_=None

 
    if request.method == "GET":
        print(request.GET)
        if 'q' in request.GET:
            q=request.GET['q']
            all=Product.objects.filter(Q(category__icontains=q)|Q(name__icontains=q)|Q(desc__icontains=q))
            if not all:
                 not_match=True
                 return render(request,'home.html',{'not_match':not_match})
        
       
        elif 'cat' in request.GET:
            cat=request.GET['cat']
            print(cat)
            all=Product.objects.filter(category=cat)

        elif 'trending' in request.GET:
            tr=request.GET['trending']
            all=Product.objects.filter(t=1)

        elif 'offer' in request.GET:
            a=request.GET['offer']
            all=Product.objects.filter(o=1)  

        else:
         all=Product.objects.all() 

    
    # Adding pagination
    paginator = Paginator(all,6)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    
    context={'all':all,'categories_list':categories_list, 'page_obj': page_obj,'count_':count_}


    return render(request,'home.html',context)


@login_required(login_url='login')
def cart_(request):
    
    a=cart.objects.filter(host=request.user)  
   
      
  

    total_a=0
    for i in a:
        total_a+=i.total_p
    print(total_a)
    

    if request.user.is_authenticated:
        count_=cart.objects.filter(host=request.user).count()
        print(count_)

    else:
        count_=None
    context={'a':a,'total_a':total_a,'count_':count_} 

    return render(request,'cart.html',context)



def knowus(request):
        
      return render(request,'knowus.html')



def support(request):


    return render(request,'support.html')

@login_required(login_url='login')
def addtocart(request,id):

    product=Product.objects.get(id=id)
     
    # print(product.name)
    try:
        c=cart.objects.get(name=product.name,host=request.user)
        c.q+=1
        c.total_p+=product.price
        c.save()
    except:
        cart.objects.create(category=product.category,name=product.name,desc=product.desc,
                            price=product.price,host=request.user,q=1,total_p=product.price,image=product.image)
 
    return redirect('cart')


def remove(request,id):

    c_i=cart.objects.get(id=id)
    c_i.delete()
    return redirect('cart')




def profile(request):
        user = request.user 
        return render(request,'profile.html',{'user':user})


def e_p(request,id):
    a=User.objects.get(id=id) 
    if request.method=='POST':
          a.first_name=request.POST['fname']
          a.last_name=request.POST['lname']
          a.email=request.POST['email']
          a.username=request.POST['uname']
          a.password=request.POST['Password']
          a.save()
          return redirect('login')
    return render(request ,'edit_p.html',{'a':a}) 


def delete_p(request,id):
    a=User.objects.get(id=id)
    a.delete()
    return redirect('register')
    

 
def checkout_(request):
    cart_items = cart.objects.filter(host=request.user)
    total_amount = sum(item.total_p for item in cart_items)  # Calculate total price

    if request.method == 'POST':
        form = ch_form(request.POST)
        if form.is_valid():
            checkout_instance = form.save(commit=False)
            checkout_instance.host = request.user
            checkout_instance.save()

            # Process order after successful payment
            for item in cart_items:
                Order.objects.create(
                    host=request.user,
                    category=item.category,
                    name=item.name,
                    q=item.q,
                    price=item.price,
                    total_p=item.total_p,
                    status='Pending',
                )
            cart_items.delete()  # Clear the cart
            return redirect('order')
    else:
        form = ch_form()

    return render(request, 'checkout.html', {'form': form, 'total_amount': total_amount})



def increase_quantity(request,id):
    q=cart.objects.get(id=id)
    q.q=q.q+1
    q.save()
    q.total_p=q.price*q.q
    q.save()
    
    return redirect('cart') 


def decrease_quantity(request,  id):
    q=cart.objects.get(id=id)
    q.q=q.q-1
    q.save()
    q.total_p=q.price*q.q
    q.save()
    return redirect('cart') 
  
    
def order(request):
    fc =checkout.objects.filter(host=request.user)     
   
    return render(request, 'order.html',{'fc':fc})



def trace_o(request):
    orders = Order.objects.filter(host=request.user)
    return render(request, 'trace_o.html',{'orders':orders})



