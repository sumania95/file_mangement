from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
import json
from django.contrib.auth import logout
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


from django.contrib.auth.models import User

class Security_Page(LoginRequiredMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'pages/security/page_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Change Password"
        return context

class Security_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        user = User.objects.get(id=self.request.user.id)
        form = PasswordChangeForm(user=user)
        context = {
            'form': form,
            'user': user,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('pages/security/page_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = PasswordChangeForm(user=self.request.user,data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('dashboard')
                logout(request)
            else:
                message = form.errors.as_json()
                y = json.loads(message)
                try:
                    title = y["new_password2"][0]["message"]
                except Exception as e:
                    pass
                try:
                    title = y["old_password"][0]["message"]
                except Exception as e:
                    pass
                print(message)
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = title

        return JsonResponse(data)
