from django.db import models
from django.core.exceptions import ValidationError

from logics.constants import ROLE_CHOICES

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    last_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True

class Employee(BaseModel):
    emp_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    need_to_accept = models.BooleanField(default=True)

class Policies(BaseModel):
    wording = models.TextField()
    policy_id = models.CharField(max_length=20)
    applicable_to = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=True)

class AcceptedPolicies(BaseModel):
    fk_policy = models.ForeignKey(
        'logics.Policies', on_delete=models.PROTECT , verbose_name="policy")
    is_periodic = models.BooleanField(default=True)
    fk_employee = models.ForeignKey(
        'logics.Employee', on_delete=models.PROTECT , verbose_name="employee")
    need_re_accept = models.BooleanField(default=False)
    is_reAccept = models.BooleanField(default=False)

