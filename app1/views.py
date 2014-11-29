from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import Post

def index(request):
    return render_to_response('home.html')

def PostsAll(request):
    posts = Post.objects.all().order_by('pub_date')
    context = {'posts': posts}
    return render_to_response('news', context, context_instance=RequestContext(request))
