from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Gq(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        if request.path != '/':
            if not request.session.has_key("LOGIN_LOCAL_FLAG"):
                request.session["msg"] = "未登录，请登录"
                return redirect(to='/')
            lifetime = settings.SESSION_COOKIE_AGE
            request.session.set_expiry(lifetime)
            request.session.clear_expired()

