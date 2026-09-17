from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from work_app.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import LoginForm
from .models import About, Blog
from django.shortcuts import get_object_or_404

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    past = About.objects.all()
    return render (request, 'blog.html', {'abouts':past})

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'home1.html')

def explore(request):
    return render(request, 'explore.html')

def more(request):
    past = About.objects.all()
    return render (request, 'more.html', {'abouts':past})

def page(request, pk):
    new = About.objects.all()
    net = Blog.objects.all()
    cost = get_object_or_404(About, pk=pk)
    return render(request, 'page.html', {
        'single_about':cost,
        'abouts':new,
        'blogs':net
    })

def cart(request):
    return render (request, 'cart.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class loginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True