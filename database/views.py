from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Score
from datetime import datetime

def calculate_score(blocks_used):
    weightage = [0, 0, 0, 20, 20, 20, 20, 20]
    best = [0, 5, 5, 5, 5, 5, 5, 5]

    score = 0
    for i in range(1, len(best)):
        if (blocks_used[i] != -1):
            score += weightage[i] * best[i] / blocks_used[i]

    return score

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

    if (used[map] > blocks) or (used[map] == -1):
        used[map] = blocks
        codes[map] = code

        instance.blocks = used
        instance.codes = codes
        instance.score = calculate_score(instance.blocks)
        instance.time = datetime.now()
        instance.save()

    return JsonResponse({'team': team, 'score': instance.score})
