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
    Outgoing_Document,
    Outgoing_Category,
)
from .forms import (
    Outgoing_DocumentForm
)

from django.utils import timezone
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


class Outgoing_Document_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/outgoing_document/page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Outgoing Document"
        context['URL_CREATE'] = reverse('outgoing_document_create')
        context['URL_TABLE'] = reverse('outgoing_document_table_api')
        context['outgoing_category'] = Outgoing_Category.objects.all().order_by('outgoing_category')
        return context

class Outgoing_Document_Create(LoginRequiredMixin,TemplateView):
    template_name = 'pages/outgoing_document/x_page_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Outgoing Document"
        context['NAV_ACTIVE'] = "outgoing_document_active"
        context['URL_CREATE'] = reverse('outgoing_document_create_api')
        return context

class Outgoing_Document_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'pages/outgoing_document/page_forms.html'
    def get(self, request):
        data = dict()
        form = Outgoing_DocumentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_submit': "button-submit",
            'btn_title': "Submit & Save",
            'URL_CREATE_UPDATE' : reverse('outgoing_document_create_api')

        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Outgoing_DocumentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = self.request.user
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('outgoing_document')
            else:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = 'Error connection found.'
        return JsonResponse(data)

class Outgoing_Document_Update(LoginRequiredMixin,TemplateView):
    template_name = 'pages/outgoing_document/x_page_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['outgoing_document'] = Outgoing_Document.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Outgoing Document"
        context['URL_UPDATE'] = reverse('outgoing_document_update_api')
        return context

class Outgoing_Document_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'pages/outgoing_document/page_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        outgoing_document = Outgoing_Document.objects.get(pk=id)
        form = Outgoing_DocumentForm(instance=outgoing_document)
        print(id)
        context = {
            'is_Create': False,
            'form': form,
            'btn_name': "warning",
            'btn_submit': "button-change",
            'btn_title': "Save Changes",
            'URL_CREATE_UPDATE' : reverse('outgoing_document_update_save_api',kwargs={'pk': id})
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Outgoing_Document_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        outgoing_document = Outgoing_Document.objects.get(pk=pk)
        if request.method == 'POST':
            form = Outgoing_DocumentForm(request.POST,request.FILES,instance=outgoing_document)
            if form.is_valid():
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('outgoing_document')
            else:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = 'Error connection found.'
        return JsonResponse(data)

class Outgoing_Document_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Outgoing_Document.objects.all()
    template_name = 'pages/outgoing_document/x_page_table.html'
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
        if category or search or start or end:
            URL_UPDATE = reverse('outgoing_document')
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(description__icontains = search),outgoing_category_id=category).count()
            record = self.queryset.filter(Q(description__icontains = search),outgoing_category_id=category).order_by('-date_issued')[int(start):int(end)]
            data['data'] = render_to_string(self.template_name,{'record':record,'start':start,'URL_UPDATE':URL_UPDATE})
        return JsonResponse(data)
