from django.http import JsonResponse
from django.utils.http import urlquote

from . import db
from django.shortcuts import redirect
from django.conf import settings

from functools import wraps


def auth_session(func):
    @wraps(func)
    def auth_session_wrapper(request, *args, **kwargs):
        if not request.session.has_key("LOGIN_LOCAL_FLAG"):
            request.session["msg"] = "未登录，请登录"

            referer = request.headers.get("referer", None)
            if referer is None:
                return redirect(to="/")
            if "X-Requested-With" in request.headers:
                return JsonResponse({"url": referer}, status=318)

            return redirect(to="/?url=" + urlquote(referer))

        lifetime = settings.SESSION_COOKIE_AGE
        request.session.set_expiry(lifetime)
        request.session.clear_expired()

        return func(request, *args, **kwargs)

    return auth_session_wrapper
