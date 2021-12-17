from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    credit = models.FloatField(null=False, blank=False, default=0)
    class Meta:
        db_table = 'user'
        constraints = [
            models.CheckConstraint(
                name='credit_greater_or_equal_0',
                check=models.Q(credit__gte=0)
            )
        ]