from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        mobile=request.POST.get('mobile','')
        description=request.POST.get('description','')
        if len(name)<2 or len(email)<3 or len(mobile)<10 or len(description)<4:
            messages.error(request, 'Please fill the form corectly')
        else:
            contact = Contact(name=name, email=email, mobile=mobile, description=description)
            contact.save()
            messages.success(request, 'Your message has been successfully sent')
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=[]
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count()==0:
        messages.warning(request, 'No search results found..Please refine your query')
    return render(request,'home/search.html',{'allPosts':allPosts,'query':query})

def handleSignUp(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')

        #Checks for signup Page

        if len(username)>10:
            messages.error(request,"USername must be under 10 characters")
            return redirect("home")
        if username.isalnum()==False:
            messages.error(request,"USername must have letters and numbers")
            return redirect("home")
        if pass1!=pass2:
            messages.error(request,"Passwords do not match")
            return redirect("home")

        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Icoder account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('Not Allowed')


def handleLogin(request):
    if request.method=='POST':
        loginUsername=request.POST['loginUsername']
        loginPassword=request.POST['loginPassword']

        user=authenticate(username=loginUsername,password=loginPassword)
        if user is not None:
            login(request,user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home')
    return HttpResponse("Login")

def handleLogout(request):
    logout(request)
    messages.success(request,"SuccessFully LogOut In")
    return redirect('home')