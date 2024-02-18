from django.shortcuts import render,HttpResponseRedirect
from .models import Task

# Create your views here.
def homePage(Request):
    if(Request.method=="POST"):
        t = Task()
        t.title = Request.POST.get("title")
        t.desc = Request.POST.get("desc")
        t.save()
        return HttpResponseRedirect("/")
    data = Task.objects.all()
    return render(Request,"index.html",{'data':data})


def updatePage(Request,id):
    data = Task.objects.get(id=id)
    if(data):
        data.status = not data.status
        data.save()
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")

def deletePage(Request,id):
    data = Task.objects.get(id=id)
    if(data):
        data.delete()
    return HttpResponseRedirect("/")

