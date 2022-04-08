from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


from application.models import (
    Incoming_Document,
    Year,
    Incoming_Category
)
from django.contrib.auth.models import User

class Dashboard_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/dashboard/page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_count'] = Incoming_Document.objects.count()
        context['category_count'] = Incoming_Category.objects.count()
        context['user_count'] = User.objects.count()
        context['year_count'] = Year.objects.count()
        total_size = Incoming_Document.objects.all()
        size = 0
        for p in total_size:
            p.file.size
            size+=p.file.size
        context['total_size'] = size
        return context
