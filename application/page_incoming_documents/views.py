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
from application.models import (
    Incoming_Document,
    Incoming_Category,
    Year,
)
from .forms import (
    Incoming_DocumentForm
)

from django.utils import timezone
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


class Incoming_Document_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/incoming_document.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Incoming_Document"
        incoming_category = Incoming_Category.objects.all().order_by('incoming_category')
        context['incoming_category'] = Incoming_Category.objects.all().order_by('incoming_category')
        context['year'] = Year.objects.all().order_by('-year')
        return context

class Incoming_Document_Create(LoginRequiredMixin,TemplateView):
    template_name = 'components/incoming_document_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Incoming_Document"
        return context

class Incoming_Document_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'forms/incoming_document_forms.html'
    def get(self, request):
        data = dict()
        form = Incoming_DocumentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit & Save",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Incoming_DocumentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = self.request.user
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('incoming_document')
            else:
                file = form.instance.file
                if not file.name.endswith('.pdf'):
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = 'Please upload pdf file only.'
                else:
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = 'Error connection found.'
        return JsonResponse(data)

class Incoming_Document_Update(LoginRequiredMixin,TemplateView):
    template_name = 'components/incoming_document_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['incoming_document'] = Incoming_Document.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Incoming_Document"
        return context

class Incoming_Document_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'forms/incoming_document_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        incoming_document = Incoming_Document.objects.get(pk=id)
        form = Incoming_DocumentForm(instance=incoming_document)
        context = {
            'form': form,
            'incoming_document':incoming_document,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Save Changes",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Incoming_Document_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        incoming_document = Incoming_Document.objects.get(pk=pk)
        if request.method == 'POST':
            form = Incoming_DocumentForm(request.POST,request.FILES,instance=incoming_document)
            if form.is_valid():
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('incoming_document')
            else:
                file = form.instance.file
                if not file.name.endswith('.pdf'):
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = 'Please upload pdf file only.'
                else:
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = 'Error connection found.'

        return JsonResponse(data)

class Incoming_Document_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Incoming_Document.objects.all()
    template_name = 'tables/incoming_document_table.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            if self.request.GET.get('category'):
                category = self.request.GET.get('category')
            else:
                category = None
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            category = None
            search = None
            start = None
            end = None
        print(category)
        if category or search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(description__icontains = search),incoming_category_id=category).count()
            incoming_document = self.queryset.filter(Q(description__icontains = search),incoming_category_id=category).order_by('description')[int(start):int(end)]
            data['data'] = render_to_string(self.template_name,{'incoming_document':incoming_document,'start':start})
        return JsonResponse(data)
