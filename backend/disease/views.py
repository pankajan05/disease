from django.http import HttpResponse
from django.shortcuts import render
import joblib

reloadModel = joblib.load('./model/RFModelforMPG.pkl')

def index(request):
    return render(request, 'index.html');

def predictDisease(request):
    if request.method == 'POST':
        print(request.POST.dict())
    return  None;
