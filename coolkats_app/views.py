from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from coolkats_app.models import Mentor
from django.db.models import Q
# Create your views here.


def index(request):
    field = request.GET.get('field')
    if field==None:
        field="/"
    motivation = request.GET.get('motivation')
    if motivation==None:
        motivation="/"
    mentors = Mentor.objects.filter(Q(fields__icontains=field) & Q(motivations__icontains=motivation))

    fields = ["Software Engineer", "Design", "Marketing", "Product Management"]
    motivations = ["Job search", "Career advice", "Leadership", "Mentorship", "Skills"]
    context = {
        'mentors': mentors,
        'fields':fields,
        'motivations': motivations
    }
    return render(request, 'coolkats_app/index.html', context)


def detail(request, mentor_name):
    mentor = Mentor.objects.get(name=mentor_name)
    context = {
        'mentor': mentor
    }
    return render(request, 'coolkats_app/detail.html', context)

def resources(request):
    
    return render(request, 'coolkats_app/resources.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Username/Password is incorrect')
    context={}
    return render(request, 'coolkats_app/signin.html', context)        

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('/signin/')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'coolkats_app/signup.html', context)

def logout(request):
    logout(request)
    return redirect('/signin/')

