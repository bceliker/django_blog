from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="user:login")
def index(request):
    context={
        "Aciklama":"Rakamlar Toplamda 10 adettir.",
        "numbers": [1,2,3,4,5,6,7,8,9]
    } 
    return render(request,"article/index.html",context=context)

@login_required(login_url="user:login")
def about(request):
    return render(request,"article/about.html")

@login_required(login_url="user:login")
def dashboard(request):
    art =article.objects.filter(author = request.user).order_by('-id')
    context = {
        "articles":art 
    }
    return render(request,"article/dashboard.html",context=context)

@login_required(login_url="user:login")
def addarticle(request):
    
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        art = form.save(commit=False)
        art.author = request.user
        art.save()
        messages.success(request,"Makale başarıyla kayıt edildi")
        return redirect("art:index")
    context = {
        "form":form
    }
    return render(request,"article/addarticle.html",context=context)

@login_required(login_url="user:login")
def detail(request,id):
    #art = article.objects.filter(id=id).first()
    art = get_object_or_404(article,id=id)
    comm = art.comments.all()
    context = {
        "article":art,
        "comments" : comm
    }
    return render(request,"article/detail.html",context=context)

@login_required(login_url="user:login")
def articleUpdate(request,id):
    art = get_object_or_404(article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=art)
    if form.is_valid():
        art = form.save(commit=False)
        art.author = request.user
        art.save()
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("art:dashboard")

    context = {
        "form":form
    }
    return render(request,"article/update.html",context=context)

@login_required(login_url="user:login")
def articleDelete(request,id):
    art = get_object_or_404(article,id=id)
    art.delete()
    messages.success(request,"Kayıt Başarıyla Silindi")
    return redirect("art:dashboard")

@login_required(login_url="user:login")
def articles(request):
    keyword = request.GET.get("keyword")
    print(keyword,"*************************************************************************")
    if keyword:
        art = article.objects.filter(title__contains = keyword)
    else:
        art = article.objects.all().order_by("-id")
    context = {
        "articles":art 
    }
    return render(request,"article/articles.html",context=context)

@login_required(login_url="user:login")
def commentAdd(request,id):
    art = get_object_or_404(article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author, comment_content=comment_content )
        newComment.article = art
        newComment.save()
    return redirect(reverse("art:detail",kwargs={"id":id}))

