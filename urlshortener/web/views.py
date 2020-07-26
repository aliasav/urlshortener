from __future__ import unicode_literals

from django.shortcuts import render, redirect
from web.models import URL
import logging

logger = logging.getLogger(__name__)


def home_view(request):
    '''renders home page
    '''    
    template = 'home.html'
    context = {}
    return render(request, template, context)


def redirect_view(request, hash_value=None):
    '''redirection view
    - check cache
    - check secondary
    - check primary
    '''
    url = None
    kwargs = dict(
        hash_value=hash_value,
        status=URL.LIVE,
        original_url__isnull=False)
    url_qset = URL.objects.using('default').filter(**kwargs)
    # check if url is present in secondary DB
    # url_qset = URL.objects.using('secondary').filter(**kwargs)
    # if not url_qset:
    #     # check primary
    #     url_qset = URL.objects.using('default').filter(**kwargs)
    #     if url_qset:
    #         url = url_qset[0]
    # else:
    #     url = url_qset[0]
    if not url_qset:
        return render(request, '404.html', {})

    url = url_qset[0]

    # redirect
    return redirect(url.original_url)
