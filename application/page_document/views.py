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
    Document,
    Category,
    Year,
)
from .forms import (
    DocumentForm
)

from django.utils import timezone
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


class Document_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/document.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Document"
        context['category'] = Category.objects.all().order_by('category')
        context['year'] = Year.objects.all().order_by('-year')
        return context

class Document_Create(LoginRequiredMixin,TemplateView):
    template_name = 'components/document_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Document"
        return context

class Document_Create_AJAXView(LoginRequiredMixin,View):
    template_name = 'forms/document_forms.html'
    def get(self, request):
        data = dict()
        form = DocumentForm()
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
            form = DocumentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = self.request.user
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('document')
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

class Document_Update(LoginRequiredMixin,TemplateView):
    template_name = 'components/document_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['document'] = Document.objects.get(id = id)
        except Exception as e:
            pass
        context['title'] = "Update Document"
        return context

class Document_Update_AJAXView(LoginRequiredMixin,View):
    template_name = 'forms/document_forms.html'
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        document = Document.objects.get(pk=id)
        form = DocumentForm(instance=document)
        context = {
            'form': form,
            'document':document,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Save Changes",
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)

class Document_Update_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data = dict()
        document = Document.objects.get(pk=pk)
        if request.method == 'POST':
            form = DocumentForm(request.POST,request.FILES,instance=document)
            if form.is_valid():
                form.save()
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('document')
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

class Document_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Document.objects.all()
    template_name = 'tables/document_table.html'
    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            category = self.request.GET.get('category')
            year = self.request.GET.get('year')
            start = self.request.GET.get('start')
            end = self.request.GET.get('end')
        except KeyError:
            category = None
            year = None
            search = None
            start = None
            end = None
        print(category)
        print(year)
        if category or year or search or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(description__icontains = search),category_id = category,year_id = year).count()
            document = self.queryset.filter(Q(description__icontains = search),category_id = category,year_id = year).order_by('description')[int(start):int(end)]
            data['data'] = render_to_string(self.template_name,{'document':document,'start':start})
        return JsonResponse(data)
