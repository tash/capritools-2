from base64 import b64decode

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout

from capritools2.stuff import render_page


def home(request):
    return render_page(
        "capritools2/home.html",
        {},
        request
    )


def theme_submit(request, theme, ret):
    request.session['theme'] = theme
    return redirect(b64decode(ret))
