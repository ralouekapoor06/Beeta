
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views import generic

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.contrib.auth import login as auth_login
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm

from django.contrib.auth.models import Group, User


from django.contrib.auth import update_session_auth_hash





def Stuck(request):
    return render_to_response(
        'stuck/stuck.html',
    )




def predict1(request):
    return render_to_response(
        'machine/machineform.html',
    )


def What2(request):    
    name = request.POST['Name']
    phone = request.POST['phone']
    age=request.POST['age']
    gender=request.POST['gender']
    emailid=request.POST['email_id']
    location=request.POST['location']



    import pyodbc 
    server = 'news1.database.windows.net' 
    database = 'newslinks' 
    username = 'raloue' 
    password = 'rk,2460..' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.Stuck (Fullname,phone,age,gender,emaiid,location) VALUES (?,?,?,?,?,?)"
    val = ("car",1223,12,"male","aghh","hhgg")
    cursor.execute(sql, val)
    print("successful execution")
    cursor.close()







    #print(age)
    context = {
        'data1':name ,
    }

    return render_to_response(
        'stuck/stuck1.html',
        context,RequestContext(request)
    )


def Entry(request):
    return render_to_response(
        'entry/entry.html',
    )

def Entry1(request):
    password1=request.POST['password']
    password1=int(password1)
    if(password1!=1234):
        return render_to_response("mainpage1/index.html")
    #print(password1)
    import pyodbc 
    server = 'news1.database.windows.net' 
    database = 'newslinks' 
    username = 'raloue' 
    password = 'rk,2460..' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.entry (place, rain,river,pass) VALUES (?, ?,?,?)"
    val = ("car",1,2,"1234")
    cursor.execute(sql, val)
    print("successful execution")
    cursor.close()

    



    city = request.POST['Name']
    if (city=='Mumbai'):
        ee='MUMBAI'
        global a1
        a1 = request.POST['rain']
        global b1
        b1=request.POST['river']
    elif(city=='Chennai'):
        ee='CHENNAI'
        global c1
        global d1
        c1 = request.POST['rain']
        d1=request.POST['river']
    elif (city=='Bhubaneswar'):
        ee='Bhubaneswar'
        global e1
        global f1
        e1 = request.POST['rain']
        f1=request.POST['river']

    context = {
        'data1': ee,
    }

    return render_to_response(
        'entry/entry1.html',
        context,RequestContext(request)
    )
#add a null condition here



def What1(request):
    name = request.POST['Name']
    phonenumber = request.POST['phone']
    location=request.POST['location']


    import pyodbc 
    server = 'news1.database.windows.net' 
    database = 'newslinks' 
    username = 'raloue' 
    password = 'rk,2460..' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    sql = "INSERT INTO dbo.Predict (Fullname,phone2,location) VALUES (?,?,?)"
    val = ("car",1,"1234")
    cursor.execute(sql, val)
    print("successful execution")
    cursor.close()


    #print(name)
    if(location=='Mumbai'):
        w1='Mumbai'
        s1=Machine(int(a1),int(b1))
    elif (location=='Chennai'):
        w1='Chennai'
        s1=Machine(int(c1),int(d1))
    elif(location=='Bhubaneswar'):
        w1='Bhubaneswar'
        s1=Machine(int(e1),int(f1))
    else:
        w1='UNknown'
        s1=Machine(4,288)
    
    context = {
        'data1': s1,
        'data2':w1,
        'data3':name
    }

    return render_to_response(
        'machine/machine.html',
        context,RequestContext(request)
    )






