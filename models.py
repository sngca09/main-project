from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class add_employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    age = models.CharField(max_length=100,null=True)
    experience = models.CharField(max_length=100,null=True)
    technology = models.CharField(max_length=100,null=True)
    employee_id= models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class trainer_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    age = models.CharField(max_length=100,null=True)
    experience = models.FileField('file/',null=True)
    technology = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)


class Technology(models.Model):
    technology_name =models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    status1 = models.CharField(max_length=100,null=True)
    status2=models.CharField(max_length=100,null=True)

class Request_technology(models.Model):
    employee = models.ForeignKey(add_employee, on_delete=models.CASCADE, null=True)
    technology= models.ForeignKey(Technology, on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=100,null=True)
    status1 = models.CharField(max_length=100,null=True)

class time_schedule(models.Model):
    trainer = models.ForeignKey(trainer_reg, on_delete=models.CASCADE, null=True)
    technolog= models.ForeignKey(Technology, on_delete=models.CASCADE, null=True)
    technology_name= models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    start_time=models.CharField(max_length=100,null=True)
    end_time=models.CharField(max_length=100,null=True)
    last_update = models.DateTimeField(auto_now=True,null=True)

    meeting_link=models.CharField(max_length=100,null=True)

    status=models.CharField(max_length=100,null=True)

# class Recorded_class(models.Model):
#     trainer = models.ForeignKey(trainer_reg, on_delete=models.CASCADE, null=True)
#     time_sche= models.ForeignKey(time_schedule, on_delete=models.CASCADE, null=True)
#     video= models.FileField('file/',null=True)
#     status=models.CharField(max_length=100,null=True)

class upload_notes(models.Model):
    trainer = models.ForeignKey(trainer_reg, on_delete=models.CASCADE, null=True)
    notes = models.FileField('file/',null=True)
    note_name =models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)

class recorded_class(models.Model):
    trainer = models.ForeignKey(trainer_reg, on_delete=models.CASCADE, null=True)
    video = models.FileField('file/',null=True)
    video_name = models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)

class Questions(models.Model):
    technology = models.ForeignKey(Technology,on_delete=models.CASCADE,null=True)
    Question1 =  models.CharField(max_length=400,null=True)
    answer1= models.CharField(max_length=400,null=True)
    options1 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question2 =  models.CharField(max_length=400,null=True)
    answer2= models.CharField(max_length=400,null=True)
    options2 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question3 =  models.CharField(max_length=400,null=True)
    answer3= models.CharField(max_length=400,null=True)
    options3 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question4 =  models.CharField(max_length=400,null=True)
    answer4= models.CharField(max_length=400,null=True)
    options4 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    Question5 =  models.CharField(max_length=400,null=True)
    answer5= models.CharField(max_length=400,null=True)
    options5 = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)
    status = models.CharField(max_length=30,null=True)
    expire = models.CharField(max_length=30,null=True)

class Answers(models.Model):
    emoployee = models.ForeignKey(add_employee,on_delete=models.CASCADE,null=True)
    qns = models.ForeignKey(Questions,on_delete=models.CASCADE,null=True)
    Question1 =  models.CharField(max_length=400,null=True)
    answer1= models.CharField(max_length=400,null=True)
    Question2 =  models.CharField(max_length=400,null=True)
    answer2= models.CharField(max_length=400,null=True)
    Question3 =  models.CharField(max_length=400,null=True)
    answer3= models.CharField(max_length=400,null=True)
    Question4 =  models.CharField(max_length=400,null=True)
    answer4= models.CharField(max_length=400,null=True)
    Question5 =  models.CharField(max_length=400,null=True)
    answer5= models.CharField(max_length=400,null=True)
    status = models.CharField(max_length=30,null=True)
    expire = models.CharField(max_length=30,null=True)

class chat(models.Model):
    employee = models.ForeignKey(add_employee, on_delete=models.CASCADE, null=True)

    message = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    reply = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)












