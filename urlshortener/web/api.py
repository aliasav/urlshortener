# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .serializers import URLSerializer
from web.models import URL

logger = logging.getLogger(__name__)


class URLDetailAPI(APIView):
    '''URL Item Detail API
    '''
    def get(self, request, hash_value):
        '''return data for a hash
        '''
        url_qset = URL.objects.filter(hash_value=hash_value)
        if not url_qset:
            return Response(status=status.HTTP_400_BAD_RESPONSE)
        url = url_qset[0]
        return Response(data=url.get_json())

    def post(self, request):
        '''created a URL object
        '''
        # To Do
        return Response(status=status.HTTP_200_OK)
