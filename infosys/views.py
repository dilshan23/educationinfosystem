from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Greeting,Post,BlogComments
from .forms import BlogCommentsForm
from .filters import UserFilter,BlogFilter


import random

from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#dil
from pymongo import *
import pandas as pd
from matplotlib import pyplot as plt
from  bokeh.plotting import figure ,output_file,show
from bokeh.embed import components


import pandas as pd
import datetime as dt




def search(request):
    #user_list = User.objects.all()
    message_list = BlogComments.objects.all()

    #user_filter = UserFilter(request.GET, queryset=user_list)
    message_filter = BlogFilter(request.GET,queryset=message_list)

    return render(request, 'search_userlist.html', {'filter': message_filter})



def showform(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')   ## dil -----yay !!!
    context= {'form': form }
        
    return render(request, 'contact.html', context)



# Create your views here.
def index(request):

    context = {
     'posts':Post.objects.all()
    }


    # get data from sqlite.db and convert to a pandas df and push to mlab cloud db

    dataposts1=Post.objects.first() #first row ,first column value

    #content1 =dataposts1.content  #first row ,second olumn value


    print(dataposts1)

   

    






    #postsDf = pd.DataFrame(Post.objects.all)
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html",context)

def schools(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "schools.html")

def research(request):

    
    return render(request, "cddsd.html")

def dea(request):

    
    return render(request, "dea.html")





def visuals(request):

    s = [1,4,6,8]

    print(s)


    h = [1,5,9,8]

    p = figure(plot_width=600, plot_height=600)
    p.vbar(x=s, width=0.5, bottom=0,
       top=h, color="black")
    #script, div = components(p)
    

    MONGODB_URI = ""
    client = MongoClient(MONGODB_URI, connectTimeoutMS=1900000)
    db = client.get_database("")

    students =  list(db.vibagas.find() )#dil
    data = pd.DataFrame(students)

    columnnames = list(data.head(0))


    print(columnnames)

    data['grade5'] = pd.to_numeric(data.grade5)

    data['year'] = pd.to_numeric(data.year)


    #flights['arr_delay'].describe()
    stat = data['grade5'].describe()
    print(stat)

    p1 = figure(plot_width =600,plot_height =600)
    p1.quad(bottom=0,top=data['grade5'],left = 0,right = 200)

    p2 = figure(plot_width =600,plot_height =600)
    p2.square(data['year'],data['grade5'])

    script,div = components(p2)

    script1,div1 = components(p)

    





    #p.vbar(x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', source=source, width=0.70, color=color_map)



    

    #print(students)


    return render(request, 'dashvisuals.html', {'div': div, 'script': script,'div1':div1,'script1':script1})


def experimentalstudies(request):
    MONGODB_URI = ""
    client = MongoClient(MONGODB_URI, connectTimeoutMS=1900000)
    db = client.get_database("")


   


    
    students =  list(db.people.find() )#dil
    teachers = list(db.gurus.find())
    exams = list(db.vibagas.find())
    tests = list(db.tests.find())

    df1 = pd.DataFrame(students)



    #calculating age
    
    now = dt.date.today().year
    print(now)

    #print(now.date())
    df7 = pd.DataFrame()
    df7['birthdate'] = pd.to_datetime(df1['birthdate'])
    df1['birthyear'] = pd.to_datetime(df7['birthdate'], format='%y/%m/%d').dt.year

    """df1['birthdate'] = pd.to_datetime(df1['birthdate'], format='%Y%m%d')
                 df1["Age"] = (now.date() - df1['birthdate']).astype('<m8[Y]')
                 print(df1)""" 

    #df1.birthdate.dt.strftime('%Y%m%d').astype(int)

    #df7["Age"] = (now1.date() - df7['birthdate'])


    print(df1['birthyear'])

    df1["Age"] = (now - df1['birthyear'])

    print(df1.Age)


    df2 = pd.DataFrame(exams)

    #print(df2)

    #df2.to_csv('exams.csv')

    df1.rename(columns={'id': 'studentId'}, inplace=True)

    df1 = df1.drop("__v", axis=1)
    df1 = df1.drop("_id",axis =1)
    df2 = df2.drop("_id",axis =1)
    df2 = df2.drop("__v", axis=1)

    #data['grade5'] = pd.to_numeric(data.grade5)
    df1['studentId'] = pd.to_numeric(df1.studentId)
    df2['studentId'] = pd.to_numeric(df2.studentId)


    


    dfjoined = pd.merge(df2,df1,on= 'studentId')

    dfjoined['school'] = 'Alakolawewa Vidyalaya'



    #dfnew = df1.merge(df2, on='mukey', how='left')


   
    #dfjoined.to_csv('exams1.csv')


    examsjoined = dfjoined.to_dict(orient = 'records')
    #print(examsjoined)
   
    #print(students)
    """context = {
                   'data1':students,
            
                }"""

    # cleaning tests data table
    df4 = pd.DataFrame(tests)
    df4.rename(columns={'stu': 'studentId'}, inplace=True)
    df4['studentId'] = pd.to_numeric(df4.studentId)

    testsjoined = pd.merge(df4,df1,on= 'studentId')
    testsjoined = testsjoined.to_dict(orient = 'records')

    #make a function in future --add school name
    df1['school'] = "Alakolawewa Vidyalaya"
    students = df1.to_dict(orient = 'records')
    


   
    return render(request, "experimentalstudies.html",{'data1':students,'data2':teachers,'data3':examsjoined,'data4':testsjoined})


def simulateddata(request):

    MONGODB_URI1 = ""
    client1 = MongoClient(MONGODB_URI1, connectTimeoutMS=1900000)
    db1 = client1.get_database("walapane")

    alltests = list(db1.termtests.find())

    return render(request, "simulateddata.html",{'data5':alltests})


def quiz(request):
     MONGODB_URI = ""
     client = MongoClient(MONGODB_URI, connectTimeoutMS=1900000)
     db = client.get_database("walapane")
            
                
     quizusers = list(db.quizusers.find())
     quizquiz = list(db.quizquiz.find())
     quizsitting = list(db.quizsitting.find())

     

     return render(request, "quizdata.html",{'data1':quizusers,'data2':quizquiz,'data3':quizsitting})





def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect("index")
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'login.html', {})




def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    print('logout function working')
    return redirect('login')

