import json
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers)}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


def suma(request, a, b):
    response = {
        'resultado': int(a) + int(b)
    }
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers),
                            'body': request.body.decode()}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_suma(request):
    body = json.loads(request.body.decode())
    a = body["a"]
    b = body["b"]

    response = {
        'resultado': int(a) + int(b)
    }
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


def gallery(request):
    return render(request, 'testapp/gallery.html')


def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)
