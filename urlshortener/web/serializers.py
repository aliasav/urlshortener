import logging

from django.conf import settings
from rest_framework import serializers

from . import models

logger = logging.getLogger(__name__)


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = (
            'id', 'original_url', 'short_url', 'status', 'expiry', 'created_at',)
