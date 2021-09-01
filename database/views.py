from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
    print(request.body)
    payload = json.loads(request.body)
    print(payload)
    return JsonResponse({'success': 'True'})
