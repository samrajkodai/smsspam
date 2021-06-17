from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request,'index.html')

def result(request):
    email=request.GET['email']
    pred=ml_predict.prdict(email)
    pred="this message is {} message".format(pred)
    return render(request,'result.html',{"pred":pred})