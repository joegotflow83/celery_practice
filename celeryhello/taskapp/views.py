from django.shortcuts import render
from django.http import HttpResponse

from taskapp.tasks import stupid_math

# Create your views here.

def insane_math(request):

    for _ in range(100):
        stupid_math.delay()
    return HttpResponse("Job Well Done I just queued 100 tasks!")
