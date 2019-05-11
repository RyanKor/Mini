from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForms, CommentForms, UserForms, SearchForm
from .models import Post, Comment, Category, Menu, Univ, Summary
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
###
from django.db.models import Q
from django.views.generic.edit import FormView
# Create your views here.
@login_required(login_url='/accounts/login/')
def new(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForms()
        return render(request, 'new.html', { 'form':form })

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForms(request.POST, request.FILES)
        comment = form.save(commit=False)
        comment.author = request.user.get_username()
        comment.post = post
        comment.save()
        return redirect('detail', post.pk)
    else:
        form = CommentForms()
        return render(request, 'detail.html', { 'post' : post, 'form': form })
        
@login_required(login_url='/accounts/login/')
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()
        return redirect('detail', post.pk)
    else:
        form = PostForms(instance=post)
        return render(request, 'edit.html', { 'form': form })
    
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForms()
            error = "이미 존재하는 아이디입니다"
            return render(request, 'registration/signup.html', {'form':form, 'error':error})
    else:
        form = UserForms()
        return render(request, 'registration/signup.html', {'form': form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    menus = Menu.objects.all()
    # posts = Post.objects.all()
    # pizza_products = Post.objects.filter(menu='pizza')
    # chicken_products = Post.objects.filter(menu='chicken')
    # bossam_products = Post.objects.filter(menu='bossam')
    # tteok_products = Post.objects.filter(menu='tteok')
    # jok_products = Post.objects.filter(menu='jok')
    # dak_products = Post.objects.filter(menu='dak')
    # sap_products = Post.objects.filter(menu='sap')
    # mara_products = Post.objects.filter(menu='mara')
    # jjim_products = Post.objects.filter(menu='jjim')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Post.objects.filter(category=category)
    return render(request, 'list.html',
                  {'category': category,
                   'categories': categories, 'products':products, 'menus':menus})

def menu_list(request, menu_slug=None):
    menu = None
    menus = Menu.objects.all()
    if menu_slug:
        menu = get_object_or_404(Menu, slug=menu_slug)
        menulist = Post.objects.filter(menu=menu)
    return render(request, 'list2.html', {'menu':menu, 'menus':menus, 'menulist':menulist})

def load_summaries(request, univ_id=None):
    univ_id = request.GET.get('univ')
    summaries = Summary.objects.filter(univ_id=univ_id)
    return render(request, 'summaries_dropdown_list_options.html', {'summaries': summaries})


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'home.html'
    def form_valid(self,form): # post method로 값이 전달 됬을 경우
        word = '%s' %self.request.POST['word'] # 검색어 
        post_list = Post.objects.filter( 
            Q(title__icontains=word) | Q(content__icontains=word) | Q(univ__name__contains=word) | Q(summary__name__contains=word) # Q 객체를 사용해서 검색한다.
        # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
        ).distinct()
        context = {}
        context['object_list'] = post_list
        # 검색된 결과를 컨텍스트 변수에 담는다. 
        context['search_word']= word # 검색어를 컨텍스트 변수에 담는다. 
        return render(self.request, self.template_name, context)