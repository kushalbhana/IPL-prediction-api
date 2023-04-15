from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def prediction(request):
    if request.method == 'POST':
        json_data= request.body

        return HttpResponse('Hii..')
