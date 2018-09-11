from django.shortcuts import render
from .models import Comentario
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# Create your views here.
from django.http import HttpResponse


def detail(request, com_id):
    return HttpResponse("Comentario número %s" % com_id)

def comments_all(request):
    comentarios_lista = Comentario.objects.all()
    #output = '\n'.join([com.contenido for com in comentarios_lista])
    template = loader.get_template('comentarios/comments_all.html')
    context = {
        'comentarios_lista' : comentarios_lista,
    }

    return HttpResponse(template.render(context, request))

def comentar(request):
    comentario = Comentario()
    #contenido
    contenido = request.POST['comment']
    comentario.contenido = contenido
    #fecha
    comentario.fecha =datetime.datetime.now()
    #ip
    ip = request.environ['REMOTE_ADDR']
    comentario.ip = ip
    comentario.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
