from django.db import models
from django.urls import reverse, reverse_lazy

class Password(models.Model):
    saved_password = models.CharField(db_column='SavedPassword', unique=True, max_length=256)
    website = models.CharField(db_column='Website', unique=True, max_length=256)
    description = models.CharField(db_column='Description', max_length=8000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "Password"
        verbose_name_plural = "Passwords"

    def __str__(self):
        return self.website

    def get_absolute_url(self):
        return reverse("password-detail", kwargs={"pk": self.pk})