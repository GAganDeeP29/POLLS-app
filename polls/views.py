# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages import add_message
from django.http import HttpResponse, HttpResponseServerError
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from mysite import settings

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def show_recent(self):
        q = models.Question.objects.order_by('-pub_date')
        return q if q is not None else StandardError("Error")


class QuestionDetailView(DetailView):
    template_name = "detail.html"
    model = models.Question
    fields = "__all__"

    def get_object(self, queryset=None):
        self.object = models.Question.objects.get(id=self.kwargs['pk'])
        return super(QuestionDetailView, self).get_object(queryset=None)








