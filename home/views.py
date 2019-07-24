from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from home.models import UserInput
import datetime


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', context=None)

    def post(self, request):
        userdata = request.POST.get('user_input');
        usermodel = UserInput(date=datetime.datetime.now(), time=datetime.datetime.now(), userinput=userdata,
                              date_time=datetime.datetime.now());
        usermodel.save();
        return HttpResponse(userdata);
