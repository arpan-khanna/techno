from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Score

@csrf_exempt
def update(request):
    payload = json.loads(request.body)

    team = payload['team']
    map = payload['map']
    blocks = payload['blocks']
    code = payload['code']

    instance = Score.objects.get_or_create(team=team)[0]
    used = instance.blocks
    codes = instance.codes

    if (used[map] >= blocks) or (used[map] == -1):
        used[map] = blocks
        codes[map] = code

    instance.blocks = used
    instance.codes = codes
    instance.save()

    return JsonResponse({'success': 'True'})
