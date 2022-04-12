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
    Ordinance_Resolution_Document,
    Ordinance_Resolution_Category
)
from .forms import (
    Ordinance_Resolution_DocumentForm
)

from django.utils import timezone
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


class Ordinance_Resolution_Document_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/ordinance_resolution_document/page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Document"
        context['URL_CREATE'] = reverse('ordinance_resolution_document_create')
        context['URL_TABLE'] = reverse('ordinance_resolution_document_table_api')
        context['category'] = Ordinance_Resolution_Category.objects.all().order_by('category')

        return context

class Ordinance_Resolution_Document_Create(LoginRequiredMixin,TemplateView):
    template_name = 'pages/ordinance_resolution_document/x_page_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Document"
        context['NAV_ACTIVE'] = "ordinance_resolution_document_active"
        context['URL_CREATE'] = reverse('ordinance_resolution_document_create_api')
        return context

class Ordinance_Resolution_Document_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'pages/ordinance_resolution_document/page_forms.html'
    def get(self, request):
        data = dict()
        form = Ordinance_Resolution_DocumentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_submit': "button-submit",
            'btn_title': "Submit & Save",
            'URL_CREATE_UPDATE' : reverse('ordinance_resolution_document_create_api')

        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Ordinance_Resolution_DocumentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = self.request.user
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('ordinance_resolution_document')
            else:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = 'Error connection found.'
        return JsonResponse(data)

class Ordinance_Resolution_Document_Update(LoginRequiredMixin,TemplateView):
    template_name = 'pages/ordinance_resolution_document/x_page_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['ordinance_resolution_document'] = Ordinance_Resolution_Document.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Document"
        context['URL_UPDATE'] = reverse('ordinance_resolution_document_update_api')
        return context

class Ordinance_Resolution_Document_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'pages/ordinance_resolution_document/page_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        ordinance_resolution_document = Ordinance_Resolution_Document.objects.get(pk=id)
        form = Ordinance_Resolution_DocumentForm(instance=ordinance_resolution_document)
        print(id)
        context = {
            'is_Create': False,
            'form': form,
            'btn_name': "warning",
            'btn_submit': "button-change",
            'btn_title': "Save Changes",
            'URL_CREATE_UPDATE' : reverse('ordinance_resolution_document_update_save_api',kwargs={'pk': id})
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Ordinance_Resolution_Document_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        ordinance_resolution_document = Ordinance_Resolution_Document.objects.get(pk=pk)
        if request.method == 'POST':
            form = Ordinance_Resolution_DocumentForm(request.POST,request.FILES,instance=ordinance_resolution_document)
            if form.is_valid():
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('ordinance_resolution_document')
            else:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = 'Error connection found.'
        return JsonResponse(data)

class Ordinance_Resolution_Document_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Ordinance_Resolution_Document.objects.all()
    template_name = 'pages/ordinance_resolution_document/x_page_table.html'
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
            URL_UPDATE = reverse('order_document')
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(description__icontains = search),category_id=category).count()
            record = self.queryset.filter(Q(description__icontains = search),category_id=category).order_by('-date_approved')[int(start):int(end)]
            data['data'] = render_to_string(self.template_name,{'record':record,'start':start,'URL_UPDATE':URL_UPDATE})
        return JsonResponse(data)
