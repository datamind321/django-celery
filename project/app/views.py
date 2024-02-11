from django.shortcuts import render
from project.celery import add 
from app.tasks import sub
from celery.result import AsyncResult

# Create your views here.

# def home(request):
#     print('Result: ')
    
#     result1 = add.delay(15,10)
#     print('result without celery: ',result1)
#     # result2 = sub.delay(15,10)  # using delay() method
#     result2 = sub.apply_async(args=[20,15])
#     print('result without celery: ',result2)
#     return render(request,'home.html')


def home(request):
    result = add.delay(20,10)
    return render(request,'home.html',{'result':result})

def check_result(request,task_id):
    result = AsyncResult(task_id)
    print('Ready: ',result.ready())
    print('Successfull: ',result.successful())
    print('Failled: ',result.failed())
    return render(request,'result.html',{'result':result})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')