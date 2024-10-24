from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb,Rubric

from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

   # template = loader.get_template ('bboard/index.html')
   # bbs = Bb.objects.order_by('-published')
   # context ={'bbs':bbs}
   # return HttpResponse(template.render(context, request))

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
class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context