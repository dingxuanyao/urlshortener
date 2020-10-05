from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_GET, require_POST
from .models import Url
from django.views.decorators.csrf import csrf_exempt
import json


def post_url(request):
    body = json.loads(request.body)
    full_url = body['full_url']
    url = Url(full_url=full_url)
    url.save()
    return JsonResponse({
        "short_id": url.short_id
    })


def short_id_from_path(path):
    print(path)
    path = path[14:]
    if path[-1] == "/":
        path = path[:-1]
    return path


def redirect_url(request):
    try:
        short_id = short_id_from_path(request.path)
        print(short_id)
        url = Url.objects.get(short_id=short_id)
        return redirect(url.full_url)
    except Url.DoesNotExist:
        return JsonResponse({'message': "URL not found"}, status=404)