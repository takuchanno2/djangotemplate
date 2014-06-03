# coding:utf-8

from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login as login_view
from django.contrib.auth.views import logout as logout_view
from django.views.generic import View
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages

class LoginView(View):
    template_name = "accounts/login.html"
    extra_context = {
        "hide_user_button": True,
    }

    def get(self, request, *args, **kwargs):
        return login_view(request, template_name=self.template_name, extra_context=self.extra_context) 

    def post(self, request, *args, **kwargs):
        # 「ログイン状態を記憶」しない場合は、セッションの有効期限をブラウザを閉じるまでに限定
        if not request.POST.get("remember_me", False):
            request.session.set_expiry(0)
        
        return login_view(request, template_name=self.template_name, extra_context=self.extra_context)

class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        was_authenticated = request.user.is_authenticated()
        response = logout_view(request, *args, **kwargs)

        if was_authenticated:
            messages.info(request, "ログアウトしました")
        
        return response
