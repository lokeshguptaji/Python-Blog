from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allposts=Post.objects.all()
    return render(request,'blog/blogHome.html',{'allposts':allposts})

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post)
    return render(request,'blog/blogPost.html',{'post':post,'comments':comments})

def postComment(request):
    if request.method=='POST':
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        comment1=BlogComment(comment=comment,user=user,post=post)
        comment1.save()
        messages.success(request,"Your messages has been posted successfully")
        return redirect("/blog/{post.slug}")

    return redirect("/")