# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os


def post_list(request):
    # return render(request, 'blog/post_list.html')
    return JsonResponse({
        'message': '안녕 파이썬, 장고',
        'items': ['파이썬', '장고', 'AWS', 'Azure'],
    }, json_dumps_params={'ensure_ascii': True})
