from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from Project_Team_App.models import UserType, trainer_reg, Technology


class IndexView(TemplateView):
    template_name='index.html'

class Trainer_Registration(TemplateView):
    template_name = 'trainer_reg.html'
    def get_context_data(self, **kwargs):
        context = super(Trainer_Registration,self).get_context_data(**kwargs)
        tech=Technology.objects.filter(status='addedd',status2='addedd')
        context['tech'] =tech
        return context

    def post(self, request,*args,**kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        age = request.POST['age']
        image= request.FILES['image']
        F = FileSystemStorage()
        files = F.save(image.name, image)
        experience= request.FILES['experience']
        Fi = FileSystemStorage()
        filess = Fi.save(experience.name, experience)
        type=request.POST['type']
        time=request.POST['time']
        technology=request.POST['technology']

        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password,first_name=name,email=email,last_name='0',is_staff='0')
        user.save()
        trainer= trainer_reg()
        trainer.user=user
        trainer.phone=phone
        trainer.address=address
        trainer.age=age
        trainer.image=files
        trainer.type=type
        trainer.time=time
        trainer.experience=filess
        trainer.technology=technology

        trainer.status='addedd'
        trainer.save()
        usertype = UserType()
        usertype.user = user
        usertype.type = "trainer"
        usertype.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})



class Login(TemplateView):
    template_name = 'login.html'
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        print(username)
        password = request.POST['password']
        users = authenticate(username=username,password=password)
        if users is not None:
            print(type(users.last_name))
            login(request,users)
            if users.last_name == '1':
                print(2)
                if users.is_superuser:
                    print(3)
                    return redirect('/admin')
                elif UserType.objects.get(user_id=users.id).type == "trainer":
                    return redirect('/trainer')
                else:
                    return redirect('/employee')

            else:
                print(4)
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})