from django.db import models
from django.contrib.postgres.fields import JSONField


class URL(models.Model):
    '''Model for short-long URL mapping
    '''
    # original absolute URL
    original_url = models.CharField(max_length=1024, null=True, blank=False, db_index=True)

    # hash value
    hash_value = models.CharField(max_length=20, null=True, blank=False, db_index=True)

    # shortened absolute URL
    short_url = models.CharField(max_length=512, null=True, blank=False, db_index=True)

    # status of the original URL website
    INIT = 0
    LIVE = 1
    BLOCKED = 2
    EXPIRED = 3
    status_choices = [
        (INIT, 'init'),
        (LIVE, 'live'),
        (BLOCKED, 'blocked'),
        (EXPIRED, 'expired'),
    ]
    status = models.IntegerField(default=0, choices=status_choices)

    # expiry datetime of the short URL
    expiry = models.DateTimeField(null=True, blank=True)

    # created at timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # meta data: hashing algorithm, origial url headers
    meta = JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f'{self.short_url}<-->{self.original_url}'

    def get_json(self):
        from .serializers import URLSerializer
        return URLSerializer(self).data
