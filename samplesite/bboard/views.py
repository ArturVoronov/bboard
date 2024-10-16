from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb,Rubric

def index(request):
    template = loader.get_template ('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context ={'bbs':bbs}
    return HttpResponse(template.render(context, request))

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics': rubrics, 'current_rubric':current_rubric}
    return render(request,'bboard/rubric_bbs.html', context)
    """s = 'Объявления\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content +'\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
"""
