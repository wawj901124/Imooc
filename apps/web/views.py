import json   #导入json

from django.shortcuts import render
from django.http.response import HttpResponse   #导入HttpResponse
from django.shortcuts import render_to_response   #导入render_to_response



# Create your views here.
def WebLogin(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        mobile = request.POST.get('password')
        data = request.GET.get('data')
        result['user'] = username
        result['mobileNum'] = mobile
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')

# def WebLogin(request):
#     if request.method == 'GET':
#         result = {}
#         username = request.GET.get('username')
#         mobile = request.GET.get('mobile')
#         data = request.GET.get('data')
#         result['user'] = username
#         result['mobileNum'] = mobile
#         result['data'] = data
#         result = json.dumps(result)
#         return HttpResponse(result,content_type='application/json;charset=utf-8')
#     else:
#         return render_to_response('login.html')
