"""
URL configuration for darkside project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import uuid
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path 
from django.views import View
from django.views.generic import TemplateView


def hello_world_view(request) -> HttpResponse:
    return HttpResponse("<h1>Hello, World!</h1>")

def parametrized_view(request, times: int) -> HttpResponse:
    content = "Test" * times 
    return HttpResponse(f"<h1>{content}</h1>)")

class TestView(View):
    def get(self, request):
        return HttpResponse("<h2>Test GET</h2>")
    
    def post(self, request):
        return HttpResponse("<h3>Test POST</h3>")
    
class ContextShowcaseView(TemplateView):
    template_name = "contexted.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["secret"] = f"it`s definetely secret: {uuid.uuid4()}"
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world_view),
    path('test/<int:times>', parametrized_view),
    path('test/<str:times>', parametrized_view),
    path('test/', TestView.as_view()),
    path('simple_template/', TemplateView.as_view(template_name='simple.html')),
    path('template/', ContextShowcaseView.as_view()),
    path('posts/', include("polls.urls"))
]
