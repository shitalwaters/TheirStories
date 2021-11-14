from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, SearchForm
from django.contrib.auth.models import User

from coolkats_app.models import Mentor
from django.db.models import Q
# Create your views here.
from coolkats_app.models import Mentor, AvailableTime
from django.db.models import Q

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            field=form.cleaned_data['field']
            motivation=form.cleaned_data['motivation']
            mentors = Mentor.objects.filter(Q(fields__icontains=field) & Q(motivations__icontains=motivation))
    else:
        form=SearchForm()
        mentors=[]
    

    fields = ["Software Engineer", "Design", "Marketing", "Product Management"]
    motivations = ["Job search", "Career advice", "Leadership", "Mentorship", "Skills"]
    context = {
        'mentors': mentors,
        'fields':fields,
        'motivations': motivations
    }
    return render(request, 'coolkats_app/index.html', context)

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

def logoutUser(request):
    logout(request)
    return redirect('/signin/')

def mentor(request, mentor_id):
    user=User.objects.get(id=request.user.id)
    mentor=Mentor.objects.get(id=mentor_id)
    sessions=AvailableTime.objects.filter(Q(mentor=mentor_id)&Q(user__isnull=True)).order_by('-startTime').reverse()
    context={"sessions":sessions, "mentor":mentor, "user": user}
    return render(request, 'coolkats_app/mentor.html', context)

def bookSession(request, user_id, mentor_id, session_id):
    user=User.objects.get(id=user_id)
    mentor=Mentor.objects.get(id=mentor_id)
    sessions=AvailableTime.objects.get(id=session_id)
    sessions.user=user
    sessions.save()
    message='You book a session with '+mentor.name+" on "+str(sessions.startTime.strftime("%m/%d/%Y, %H:%M:%S"))+"."
    messages.info(request, message)
    return redirect('/mentor/'+str(mentor_id))

def categoryPage(request):
    return render(request, 'coolkats_app/categories.html')

def mentorResult(request, result_id):
    if result_id==1:
        mentors= Mentor.objects.filter(Q(motivations__icontains='Essay Writing Help'))
    elif result_id==2:
        mentors= Mentor.objects.filter(Q(motivations__icontains='College Roadmap'))
    elif result_id==3:
        mentors= Mentor.objects.filter(Q(motivations__icontains='Interview Prep'))
    elif result_id==4:
        mentors= Mentor.objects.filter(Q(motivations__icontains='Presentation Skills'))
    elif result_id==5:
        mentors= Mentor.objects.filter(Q(motivations__icontains='Managing Stress'))
    elif result_id==6:
        mentors= Mentor.objects.filter(Q(motivations__icontains='Essay_Writing_Help'))
    else: 
        mentors=[]
    context={'mentors':mentors,}
    return render(request, 'coolkats_app/category.html', context)