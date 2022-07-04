from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.generic import TemplateView, View

from Project_Team_App.models import add_employee, UserType, Technology, trainer_reg, Request_technology, time_schedule, \
    Questions, Answers
from Project_Team_Selection import settings


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Add_Employee(TemplateView):
    template_name = 'admin/add_employee.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Employee,self).get_context_data(**kwargs)
        tech=Technology.objects.filter(status='addedd')
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
        experience=request.POST['experience']
        technology=request.POST['technology']
        employee_id=request.POST['employee_id']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password,first_name=name,email=email,last_name=1)
        user.save()
        employee= add_employee()
        employee.user=user
        employee.phone=phone
        employee.address=address
        employee.age=age
        employee.image=files
        employee.experience=experience
        employee.technology=technology
        employee.employee_id=employee_id
        employee.status='addedd'
        employee.save()
        usertype = UserType()
        usertype.user = user
        usertype.type = "employee"
        usertype.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})


class View_Employee(TemplateView):
    template_name = 'admin/view_employee.html'
    def get_context_data(self, **kwargs):
        context = super(View_Employee,self).get_context_data(**kwargs)
        view_employee = add_employee.objects.filter(user__last_name='1')
        context['view_employee']=view_employee
        return context

class Remove_Employee(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Approve_Trainer(TemplateView):
    template_name = 'admin/approve_trainer.html'
    def get_context_data(self, **kwargs):
        context = super(Approve_Trainer,self).get_context_data(**kwargs)
        approve_trainer = trainer_reg.objects.filter(user__last_name='0')
        context['approve_trainer']=approve_trainer
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        trainer=trainer_reg.objects.get(user_id=id)
        tech_name=trainer.technology
        tech=Technology.objects.get(technology_name=tech_name)
        tech.status2='trainer_addedd '
        tech.save()
        email = EmailMessage(
        user.first_name,
        'Your account approved',
        settings.EMAIL_HOST_USER,
        [user.email],
         )
        email.fail_silently = False
        email.send()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class View_Trainer(TemplateView):
    template_name = 'admin/view_trainer.html'
    def get_context_data(self, **kwargs):
        context = super(View_Trainer,self).get_context_data(**kwargs)
        view_trainer = trainer_reg.objects.filter(user__last_name='1')
        context['view_trainer']=view_trainer
        return context

class Add_Technology(TemplateView):
    template_name = 'admin/add_technology.html'
    def post(self, request,*args,**kwargs):
        technology_name = request.POST['technology_name']
        date=request.POST['date']
        tech=Technology()
        tech.technology_name=technology_name
        tech.date=date
        tech.status='addedd'
        tech.status1='addedd'
        tech.status1='request for new technology'
        tech.save()
        return render(request,'admin/admin_index.html',{'messages':"Addedd"})

    def get_context_data(self, **kwargs):
        context = super(Add_Technology,self).get_context_data(**kwargs)
        tech = Technology.objects.filter(status='addedd')
        context['tech']=tech
        return context

class Remove_Technology(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        tech = Technology.objects.get(pk=id)
        tech.status='remove'
        tech.save()
        return render(request,'admin/admin_index.html',{'messages':"Technology Removed"})

class View_Request(TemplateView):
    template_name = 'admin/request.html'
    def get_context_data(self, **kwargs):
        context = super(View_Request,self).get_context_data(**kwargs)
        view_request = Request_technology.objects.filter(status='requested')
        context['view_request']=view_request
        return context

class Approve_Request(View):
    def dispatch(self, request, *args, **kwargs):
        id2 = request.GET['id2']
        req = Request_technology.objects.get(pk=id2)
        req.status='Approved'
        req.status1='Approved'
        req.save()
        tech_id=req.technology_id
        tech=Technology.objects.get(id=tech_id)

        tech.status1='Approved'
        tech.save()
        return render(request,'admin/admin_index.html',{'messages':"Approved"})

class Time_Schedule(TemplateView):
    template_name = 'admin/time_Schedule.html'
    def get_context_data(self, **kwargs):
        context = super(Time_Schedule,self).get_context_data(**kwargs)
        time_schedule = trainer_reg.objects.filter(user__last_name='1',status='addedd')
        context['time_schedule']=time_schedule
        return context

class Time_Schedule_Trainer(TemplateView):
    template_name = 'admin/time_schedule_trainer.html'
    def get_context_data(self, **kwargs):
        context = super(Time_Schedule_Trainer,self).get_context_data(**kwargs)
        time_schedule = trainer_reg.objects.filter(user__last_name='1')
        context['time_schedule']=time_schedule
        return context

    def post(self, request,*args,**kwargs):
        id2 = request.GET['id2']
        technology_name=request.POST['technology_name']
        date=request.POST['date']
        start_time=request.POST['start_time']
        end_time=request.POST['end_time']
        meeting_link=request.POST['meeting_link']

        time_sche=time_schedule()
        time_sche.trainer_id=id2
        time_sche.technology_name=technology_name
        time_sche.date=date
        time_sche.start_time=start_time
        time_sche.end_time=end_time
        time_sche.meeting_link=meeting_link
        time_sche.save()
        trainer=trainer_reg.objects.get(id=id2)
        trainer.status='scheduled'
        trainer.save()

        return render(request,'admin/admin_index.html',{'messages':"Scheduled"})

class View_Time_Schedule(TemplateView):
    template_name = 'admin/view_time_schedule.html'
    def get_context_data(self, **kwargs):
        context = super(View_Time_Schedule,self).get_context_data(**kwargs)
        view_time_schedule = time_schedule.objects.all()
        context['view_time_schedule']=view_time_schedule
        return context

class Update_Schedule(TemplateView):
    template_name = 'admin/update_schedule.html'
    def post(self, request,*args,**kwargs):
        id2 = request.GET['id2']
        date=request.POST['date']
        start_time=request.POST['start_time']
        end_time=request.POST['end_time']
        meeting_link=request.POST['meeting_link']
        update_sche=time_schedule.objects.get(id=id2)
        update_sche.date=date
        update_sche.start_time=start_time
        update_sche.end_time=end_time
        update_sche.meeting_link=meeting_link
        update_sche.save()
        return render(request,'admin/admin_index.html',{'messages':"Updated"})

class Add_Quizz(TemplateView):
    template_name = 'admin/add_quiz.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Quizz,self).get_context_data(**kwargs)
        tech = Technology.objects.all()
        context['tech']=tech
        return context

class Add_Quizz_Qns(TemplateView):
    template_name = 'admin/add_quizz_qns.html'
    def post(self , request,*args,**kwargs):
        id2 = request.GET['id']
        Question1=request.POST['question1']
        Answer1 = request.POST['answer1']
        Option1 = request.POST['options1']
        Question2=request.POST['question2']
        Answer2 = request.POST['answer2']
        Option2 = request.POST['options2']
        Question3=request.POST['question3']
        Answer3 = request.POST['answer3']
        Option3 = request.POST['options3']
        Question4=request.POST['question4']
        Answer4 = request.POST['answer4']
        Option4 = request.POST['options4']
        Question5=request.POST['question5']
        Answer5 = request.POST['answer5']
        Option5 = request.POST['options5']

        paper = Questions()
        paper.technology_id=id2
        paper.Question1=Question1
        paper.answer1=Answer1
        OPTION1 = Option1
        OPTION11 = OPTION1.split(",", 5)
        paper.options1=OPTION11
        paper.Question2=Question2
        paper.answer2=Answer2
        OPTION2 = Option2
        OPTION22 = OPTION2.split(",", 5)
        paper.options2=OPTION22
        paper.Question3=Question3
        paper.answer3=Answer3
        OPTION3 = Option3
        OPTION33 = OPTION3.split(",", 5)
        paper.options3=OPTION33
        paper.Question4=Question4
        paper.answer4=Answer4
        OPTION4 = Option4
        OPTION44 = OPTION4.split(",", 5)
        paper.options4=OPTION44
        paper.Question5=Question5
        paper.answer5=Answer5
        OPTION5 = Option5
        OPTION55 = OPTION5.split(",", 5)
        print(OPTION55)
        paper.options5=OPTION55
        paper.status="active"
        paper.save()

        return render(request,'admin/admin_index.html',{'message':"created Successfully "})

class View_Quizz(TemplateView):
    template_name = 'admin/view_quizz.html'
    def get_context_data(self, **kwargs):
        context = super(View_Quizz,self).get_context_data(**kwargs)
        tech = Technology.objects.all()
        context['tech']=tech
        return context

class View_Quiz_Qns(TemplateView):
    template_name = 'admin/view_quiz_qns.html'
    def get_context_data(self, **kwargs):
        id2 = self.request.GET['id']
        context = super(View_Quiz_Qns,self).get_context_data(**kwargs)
        tech = Questions.objects.get(technology_id=id2)
        context['tech']=tech
        return context

class View_Answers(TemplateView):
    template_name = 'admin/view_ans.html'
    def get_context_data(self, **kwargs):
        context = super(View_Answers,self).get_context_data(**kwargs)
        view_ans = Technology.objects.all()
        context['view_ans']=view_ans
        return context

class View_Emp_Ans(TemplateView):
    template_name = 'admin/view_emp_ans.html'
    def get_context_data(self, **kwargs):
        id=self.request.GET['id']

        context = super(View_Emp_Ans,self).get_context_data(**kwargs)
        view_emp_ans = Request_technology.objects.filter(employee_id=id)
        context['view_emp_ans']=view_emp_ans
        return context

class View_Employee_Answer(TemplateView):
    template_name = 'admin/view_employee_answer.html'
    def get_context_data(self, **kwargs):
        id=self.request.GET['id']

        context = super(View_Employee_Answer,self).get_context_data(**kwargs)
        view_emp_ans = Answers.objects.get(emoployee_id=id)
        context['view_emp_ans']=view_emp_ans
        return context


















