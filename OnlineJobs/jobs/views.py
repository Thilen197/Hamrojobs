from django.contrib import messages
from django.shortcuts import render, redirect
from jobs.forms import Jobsform
from jobs.models import Jobs
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout

def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']


            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'homebased.html',{'form':form})
    else:
        return render(request, 'login.html')

def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'delivery.html',{'form':form})
    else:
        return render(request, 'login.html')

def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'educational.html',{'form':form})
    else:
        return render(request, 'login.html')

def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'field.html',{'form':form})
    else:
        return render(request, 'login.html')


def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'hotel.html',{'form':form})
    else:
        return render(request, 'login.html')


def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'office.html',{'form':form})
    else:
        return render(request, 'login.html')


def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description,user_id=user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'others.html',{'form':form})
    else:
        return render(request, 'login.html')


def jobs_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            job_name = request.POST['job_name']
            job_address = request.POST['job_address']
            contact_number = request.POST['contact_number']
            jobs_description = request.POST['jobs_description']
            user_id = request.POST['user_id']

            form = Jobs(job_name=job_name,job_address=job_address,contact_number=contact_number,jobs_description=jobs_description, user_id= user_id)

            form.save()
            return redirect('/jobs_url')
        else:
            form=Jobs()
        return render(request,'technical.html',{'form':form})
    else:
        return render(request,'login.html')



def delete_jobs(request,id):
 if request.user.is_authenticated:
    jobs= Jobs.objects.get(id=id)
    jobs.delete()
    return redirect('/showjobs')
 else:
     return render(request, 'login.html')

# Create your views here.
def showjobs(request):
        jobs=Jobs.objects.all()
        return render(request,'jobs.html',{'jobs':jobs})

def index(request):
    return render(request,'index.html')


def user_login(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user= auth.authenticate(username=username,password=password)

          if user is not None:
              auth.login(request,user)
              return redirect('/')
          else:
              messages.info(request,"Please Enter Valid Username & Password")
              return render(request,"login.html")
      else:
          return render(request,"login.html")

def delivery(request):
    return render(request,'delivery.html')
def educational(request):
    return render(request,'educational.html')
def field(request):
    return render(request,'field.html')
def homebased(request):
    return render(request,'homebased.html')
def office(request):
    return render(request,'office.html')
def others(request):
    return render(request,'others.html')
def technical(request):
    return render(request,'technical.html')
def hotel(request):
    return render(request,'hotel.html')
def jobs(request):
    return render(request,'jobs.html')

def user_signup(request):
  if request.method=='POST':
      username= request.POST['username']
      email=request.POST['email']
      password= request.POST['password']

      user= User.objects.create_user(username=username,email=email,password=password)
      user.save()
      return render(request,'login.html')


  else:
      return render(request,'signup.html')

def logout1(request):
    logout(request)
    return redirect('/')


def jobdetail(request,id):
    jobs=Jobs.objects.get(id=id)
    return render(request,'jobdetail.html',{'jobsdata':jobs})

def update_jobs_form(request,id):
    jobs=Jobs.objects.get(id=id)
    return render(request, 'Updateform.html', {'update_jobs': jobs})

# def update_jobs(request):
#    if request.method=="POST":
#        jobs.job_name = request.POST['job_name']
#        jobs.job_address = request.POST['job_address']
#        jobs.contact_number = request.POST['contact_number']
#        jobs.jobs_description = request.POST['jobs_description']

 #       jobs.save()
 #       return redirect("/showjobs")



