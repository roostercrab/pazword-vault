from django.db import models

class Password(models.Model):
    saved_password = models.CharField(db_column='SavedPassword', unique=True, max_length=256)
    website = models.CharField(db_column='Website', unique=True, max_length=256)
    description = models.CharField(db_column='Description', max_length=8000, blank=True, null=True)
