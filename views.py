from django.shortcuts import render,redirect
from django.http import HttpResponse
from readingapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

  

def homepage(request):
    queryset = book.objects.all().values()
    if request.GET.get('search'):
        queryset = queryset.filter(book_name__icontains = request.GET.get("search"))
        print(request.GET.get('search'))

    context = {'viewbook': queryset}
    return render(request, 'readingapp/homepage.html',context)
   
def show(request):
    request.method=="POST" in request.POST
    user=book.objects.all().values()
    return render(request,"readingapp/bookdata.html",{'users':user})  


def register(request):
    if request.method=="POST" and 'submit' in request.POST:
        # nm= request.POST.get('unm')
        # print(nm)
        user = book ( 
        username=request.POST.get('unm'),
        email=request.POST.get('ue'),
        book_name=request.POST.get('bn'),
        author_name=request.POST.get('an'),
        book_category=request.POST.get('bcat'),
        book_chapter=request.POST.get('cn'),
        book_pages=request.POST.get('pn'),
        book_img = request.FILES.get('bfile'),
        book_file = request.FILES.get('bpdf'))
        user.save()
        print(user)
        
    return render(request,"book.html")
@login_required(login_url="/login")
def addbook(request):
    
    if request.method == "POST" and 'submit' in request.POST:
        user=book(
        username=request.POST.get('username'),
        email=request.POST.get('email'),
        book_name=request.POST.get('book_name'),
        author_name=request.POST.get('author_name'),
        book_category=request.POST.get('book_category'),
        book_chapter=request.POST.get('book_chapter'),
        book_pages=request.POST.get('book_pages'),
        book_img = request.FILES.get('book_img'),
        book_file = request.FILES.get('book_file'))
        user.save()
        return redirect('/addbook/')
    queryset = book.objects.all().values()
    
    context = {'viewbook': queryset}
    return render(request, 'readingapp/addbook.html',context)

def deletebook(request, id):
    query= book.objects.get(id=id)
    query.delete()
    return redirect('/addbook/')

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.filter(username= username)
        if user.exists():
            return redirect('/register')
        user = User.objects.create(
        
            username = username,
            email = email 
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account Created Successfully')
        return redirect('/register')

    return render(request,"readingapp/register.html")    

# def login1(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # if not User.objects.filter(username=username).exists():
#         #     messages.error(request,'User does not exists')
#         #     return redirect('/login')
#         user = authenticate( username=username, password=password)
#         if user is None:
#            messages.error(request,'User does not exists')
#            return redirect('/login')
#         else:
#             login(request, user)
#             return redirect('/firstpage')
#     return render(request,"login.html") 
from django.contrib.auth import authenticate, login ,logout

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('/addbook/') # This line should work fine now
            # Redirect to a success page
        else:
            # Return an 'invalid login' error message.
            messages.error(request,'User does not exists')
            return redirect('/firstpage')  
    return render(request,"readingapp/login.html") 
def logout1(request):
    logout(request)
    return redirect('/login')
def vision(request):
    request.method=="POST" in request.POST
    return render(request,"readingapp/vision.html") 
def blog(request):
    request.method=="POST" in request.POST
    return render(request,"readingapp/blog.html") 
def volunteer(request):
    request.method=="POST" in request.POST
    return render(request,"readingapp/volunteer.html") 
def tc(request):
    request.method=="POST" in request.POST
    return render(request,"readingapp/T&C.html") 