from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from Project_Team_App.models import time_schedule, trainer_reg, upload_notes, recorded_class, chat


class IndexView(TemplateView):
    template_name = 'trainer/trainer_index.html'

class View_Schedule(TemplateView):
    template_name = 'trainer/view_schedule.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        id2=trainer.id
        context = super(View_Schedule,self).get_context_data(**kwargs)
        view_time_schedule = time_schedule.objects.filter(trainer_id=id2)
        context['view_time_schedule']=view_time_schedule
        return context
class Upload_Notes(TemplateView):
    template_name = 'trainer/upload_notes.html'
    def post(self , request,*args,**kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        a=trainer.id
        note_name=request.POST['note_name']
        notes=request.FILES['notes']
        fi=FileSystemStorage()
        files=fi.save(notes.name,notes)
        date=request.POST['date']
        note=upload_notes()
        note.trainer_id=a
        note.note_name=note_name
        note.notes=files
        note.date=date
        note.save()
        return render(request,'trainer/upload_notes.html',{'messages':"Note Add"})

    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        id2=trainer.id
        context = super(Upload_Notes,self).get_context_data(**kwargs)
        view_note = upload_notes.objects.filter(trainer_id=id2)
        context['view_note']=view_note
        return context

class Add_Recorded_Class(TemplateView):
    template_name = 'trainer/add_recorded_class.html'
    def post(self , request,*args,**kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        a=trainer.id
        video_name=request.POST['video_name']
        video=request.FILES['video']
        fi=FileSystemStorage()
        files=fi.save(video.name,video)
        date=request.POST['date']
        vido=recorded_class()
        vido.trainer_id=a
        vido.video_name=video_name
        vido.video=files
        vido.date=date
        vido.save()
        return render(request,'trainer/upload_notes.html',{'messages':"Note Add"})
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        id2=trainer.id
        context = super(Add_Recorded_Class,self).get_context_data(**kwargs)
        view_video = recorded_class.objects.filter(trainer_id=id2)
        context['view_video']=view_video
        return context

class Chat(TemplateView):
    template_name = 'trainer/chat.html'
    def get_context_data(self, **kwargs):
        id1=self.request.user.id
        trainer=trainer_reg.objects.get(user_id=id1)
        id2=trainer.technology
        context = super(Chat,self).get_context_data(**kwargs)
        chat_mes = chat.objects.filter(employee__technology=id2,status='addedd')
        context['chat_mes']=chat_mes
        return context
    def post(self , request,*args,**kwargs):
        id5=request.POST['id5']
        reply=request.POST['reply']
        mess=chat.objects.get(id=id5)
        mess.reply=reply
        mess.status='replayed'
        mess.save()
        return render(request,'trainer/trainer_index.html',{'messages':"message send"})



















