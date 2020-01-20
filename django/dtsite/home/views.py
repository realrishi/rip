from django.shortcuts import render,HttpResponse,redirect
from home.models import Cont
from blog.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

# Create your views here.

def home(request):
    homeposts=Post.objects.all()
    context={'homeposts':homeposts}
    return render(request,'home/home.html',context)


def about(request):
    return render(request,'home/about.html')


def contact(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']       
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Sorry ,please fill the form in a right manner')
        else:
            contact=Cont(name=name,email=email,phone=phone,desc=content)
            contact.save()
            messages.success(request, 'Form submitted successfully')       
    return render(request,'home/contact.html')
    
    

def search(request):
    querry = request.GET['querry']
    if len(querry)>78:
        SPPosts =Post.objects.none()
    else:
        SPPostsTitle = Post.objects.filter(title__icontains=querry)
        SPPostsContent = Post.objects.filter(content__icontains=querry)
        SPPosts = SPPostsTitle.union( SPPostsContent)
    if SPPosts.count() == 0: 
      messages.warning(request,"No search Results found .please refine Your query")
    params = {'SPPosts':SPPosts, 'querry': querry}
    return render(request, 'home/search.html',params) 


def handleLogin(request):
    if request .method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request," Successfully Logged In")
            return redirect('/blog')

        else:
            print("successfully login bro")
            messages.error(request,"invalid credentials, Plese Try Again:")
            return redirect('home')

    return HttpResponse('404 is page not found For Login page')     



    
def handleLogout(request):
    logout(request)
    messages.success(request," Successfully Logged Out")
    return redirect('home')




def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneouus inputs

        if len(username) > 10:
            messages.error(request,"username must be under 10 chracters")
            return redirect('home')

        
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return redirect('home')
        

        if pass1 != pass2:
            messages.error(request," Password Do Not Matched")
            return redirect('home')


        # create the user 
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'your Account is SptechGuru has been successfully createed')
        return redirect('/')

    else:
        return HttpResponse('404 is page not found')

