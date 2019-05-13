# 멋쟁이 사자처럼 7기 미니해커톤

####  3조 아나뿜다(아껴쓰고, 나눠쓰고, 뿜빠이하고, 다시쓰기)

![image](https://user-images.githubusercontent.com/40455392/57601868-9feb7d80-7598-11e9-8c29-1d0326ea611b.png)



## 팀원 소개, Likelion 7기

##### `김준태`: Full-Stack, Django & HTML, CSS ([elksha](https://github.com/elksha))

##### `김승태`: Back-End, Django ([RyanKor](https://github.com/RyanKor))

##### `최주원`: Front-End, HTML&CSS ([hoiJuwon](https://github.com/hoiJuwon))

##### `이유나`: Front-End, HTML&CSS ([YUNALEEEE](https://github.com/YUNALEEEE))

##### `안태경`: Front-End, HTML&CSS ([gaetokk](https://github.com/gaetokk))

![image](https://user-images.githubusercontent.com/40455392/57598917-07e99600-7590-11e9-8ff7-d99792fd8558.png)



## **Project Outline**

- 1인 가구가 증가하는 대한민국. 많은 한국인들이 식품이나 물건 등을 구매하는데 이미 대가족에 초점을 맞춘 상품들을 지양하고 1인, 소규모로 구매하는 성향이 강해지고 있습니다.
- 에어프라이어, 1인 밥솥, 소형 와인 냉장고 등 다양한 1인 커스터마이징 제품을 판매하는 것이 지금 대한민국인데 우리는 왜 아직도 식료품, 휴지 등의 제품들을 1인 가구에 맞춰 구매할 수 없을까요? 그리고 왜 야식은 1인식을 구매하면 그보다 많이 구매할 때 더 돈을 지불할 수 밖에 없을까요?
- 그래서 아나뿜다는 생각했습니다. `뿜빠이`하자! 나와 똑같은 필요에 소비하는 사람들을 모으면 서로 가져갈 물건을 지불한 액수만큼 동일하게 나눠갖고 1인을 위한 보다 합리적인 소비를 할 수 있을 것이라 판단했습니다.
- 아나뿜다는 치킨, 피자, 족발, 휴지, 식료품 등을 모두 뿜빠이 할 수 있으며 지역 기반으로 여러분과 동일한 니즈를 갖고 있는 사람들을 찾을 수 있습니다. 어서 뿜빠이하세요!



---



## **Stack**

- `Front`: HTML, CSS, JS

- `Back`: Django

  ![프레젠테이션1](https://user-images.githubusercontent.com/40455392/57599766-c73f4c00-7592-11e9-97ff-1b2b08ab4478.png)

## **Specific Stack Requirement**



-  `검색기능`: Ajax, Haystack, Whoosh 기반으로 게시글에 작성된 단어들을 중심으로 검색하게끔 유도. 밑의 코드는 views.py, home.html에 작성된 코드

```python
#models.py
class SearchForm(forms.Form):
     word = forms.CharField(label='')
```

```python
#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForms, CommentForms, UserForms, SearchForm
from .models import Post, Comment, Category, Menu, Univ, Summary
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
###
from django.db.models import Q
from django.views.generic.edit import FormView

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
```

```html
<-- home.html !-->
<div class="bigcategory">
        {% if object_list %} 
        {% for post in object_list %} 
        <div class="category" style="position: relative; width: 400px;">
            <div class="rectangle">
                <a href="{% url 'detail' post.pk %}" style="color:black;">{{ post.title }}</a>
            </div>
        </div> 
        {% endfor %} 
        {% elif search_word %} 
              Search Word {{ search_word }} Not Found!
        {% else %}
        <!-- <a href=""> -->
            <div class="category">
                <div class="rectangle">
                    <img src="" alt="">
                    <p class="category-intro">혼자 사면 비싼 생필품, 혼자가 아니라면?</p>
                    <p class="category-name">생필품</p>
                </div>
            </div> 
        </a>
        
        <!-- <a href=""> -->
            <div class="category">
                    <div class="rectangle">
                        <img src="" alt="">
                        <p class="category-intro">혼자 먹기 버거운 야식, 혼자가 아니라면?</p>
                        <p class="category-name">야식</p>
                    </div>
            </div>
        </a>

        <!-- <a href=""> -->
            <div class="category">
                    <div class="rectangle">
                        <img src="" alt="">
                        <p class="category-intro">혼자 사면 넘쳐나는 식재료, 혼자가 아니라면?</p>
                        <p class="category-name">식재료</p>
                    </div>
            </div>
        </a>

        <div class="category">
            <div class="rectangle">
                <img src="" alt="">
                <p class="category-intro">혼자 사면 많은 간식, 혼자가 아니라면?</p>
                <p class="category-name">간식</p>
            </div>
        </div>

        <div class="category">
            <div class="rectangle">
                <img src="" alt="">
                <p class="category-intro">한번 쓰고 버리기 아까운 것들, 나눌 수 있다면?</p>
                <p class="category-name">다시쓰기</p>
            </div>
        </div>
</div>
    <!-- //bigcategroy -->
    {% endif %}
```



-  `login`, `signup`, `logout`: Django 내장 Library 기반 Auth 통신 구현. 커스터마이징 된 코드 없음.

```python
#views.py, signup
from django.contrib import auth
from django.contrib.auth.models import User

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
```

```python
# forms.py, @login_required를 위한 값 설정
#유저 정보를 저장하기 위한 Form
from django.contrib.auth.models import User
class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
```

```html
<-- registration/login.html !-->
<div class="login-form">
    <form method="POST">
        {% csrf_token %}
        <div class="login-title">
            <h2>로그인</h2>
        </div>
        <div class = "login-content" >
            <p><label for="id_username">아이디</label>
                {{ form.username }}</p>
            <p><label for="id_password">비밀번호</label>
                 {{ form.password }}</p>    
            <button type="submit" class="btn btn-outline-secondary">로그인</button>
        </div>
    </form>
</div>
```

```html
<-- registration/signup.html !-->
<div class = "signup-form">
    <form method="POST">
      {% csrf_token %}
      {% if error %}
      {{ error }}
      {% endif %}
      <div class = "signup-title">
          <h2>회원가입</h2>
      </div>
      <div class = "signup-content" >
          <p><label for="id_username">아이디</label>
              {{ form.username }}</p>
          <p><label for="id_password">비밀번호</label>
              {{ form.password }}</p>    
          <button type="submit" class="btn btn-outline-secondary">확인</button>
      </div>
    </form>
</div>
```



-  메뉴에 따른 `Category` 목록 : Class Inheritance 사용. 난이도가 상당함

```python
#models.py
class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
    
### models.py, post에서 카테코리 상속
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='product')
```

```python
#views.py
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    menus = Menu.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Post.objects.filter(category=category)
    return render(request, 'list.html',
                  {'category': category,
                   'categories': categories, 'products':products, 'menus':menus})
```



-  `Menu` 기능 구현(카테고리 내 세부 메뉴 기능 추가)

```python
#models.py
class Menu(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_menu', args=[self.slug])
    
### models.py post에서 menu inheritance
class Post(models.Model):
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE, related_name='menulist')
```

```python
#views.py
def menu_list(request, menu_slug=None):
    menu = None
    menus = Menu.objects.all()
    if menu_slug:
        menu = get_object_or_404(Menu, slug=menu_slug)
        menulist = Post.objects.filter(menu=menu)
    return render(request, 'list2.html', {'menu':menu, 'menus':menus, 'menulist':menulist})
```



-  지역 기반 `Sub-Choices` 기능 구현: Class Inheritance, Jquery 사용. 미니톤 내내 제일 어려웠음.

```python
#models.py Univ class를 Summary가 상속받는 형태로 작성.
class Univ(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name

class Summary(models.Model):
    univ = models.ForeignKey(Univ, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
```

```python
#forms.py
class PostForms(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'menu', 'univ', 'summary',)
        widgets = {
            'title' : forms.TextInput(attrs = {'placeholder':'입력해주세요'}),
        }
        labels = {
            'title' : '',
            'content' : '',
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].queryset = Summary.objects.none()

        if 'univ' in self.data:
            try:
                univ_id = int(self.data.get('univ'))
                self.fields['summary'].queryset = Summary.objects.filter(univ_id=univ_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['summary'].queryset = self.instance.univ.summary_set.order_by('name')
```

```python
#views.py
def load_summaries(request, univ_id=None):
    univ_id = request.GET.get('univ')
    summaries = Summary.objects.filter(univ_id=univ_id)
    return render(request, 'summaries_dropdown_list_options.html', {'summaries': summaries})
```

```html
<-- new.html !-->
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script>
    $("#id_univ").change(function () {
      var url = $("#postForm").attr("data-summaries-url");  // get the url of the `load_cities` view
      var univId = $(this).val();  // get the selected country ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'univ': univId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
          $("#id_summary").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });

    });
    </script>
```



-  `1:N DB` :  댓글 기능 구현에 사용

```python
#models.py
class Comment(models.Model):
    #On_delete는 이 댓글이 속한 포스트가 삭제 되었을 때 어떻게 할 것인가에 대한 행동 지시
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name = 'comments')
    content = models.CharField(max_length = 500)
    # photo = models.FileField(null = True)
    def __str__(self):
        return self.content
```

```python
#forms.py
#댓글 형성 Form
class CommentForms(forms.ModelForm):
    comment = forms.CharField (widget = forms.TextInput (attrs = {'placeholder': '댓글을 입력하세요.'}), label = '')
    class Meta:
        model = Comment
        fields = ['content',]
```

```html
<-- detail.html comment 형성 !-->
<div class="commentform">
        <h3 style="font-weight:bold">댓글</h3>
        <div class="commentlist">
            <ul>
            {% for comment in post.comments.all %}
                <li>{{ comment.content }}
                    {% if user.is_authenticated and comment.author == user.username %}
                    <a href="{% url 'delete_comment' post.pk comment.pk %}">
                        <img src="https://www.flaticon.com/free-icon/garbage_126468#term=trash%20can&page=1&position=2" width="5%" height="5%" />
                    </a>
                    {% endif %}
                </li>   
            {% endfor %}
            </ul>
        </div>
        
        <div class="comment">
            <form method="POST" class="inputcomment">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="button">올리기</button>
            </form>
        </div>
</div>
```

