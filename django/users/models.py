from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class User(AbstractUser):
#     is_student = models.BooleanField()
#     is_teacher = models.BooleanField()
#     is_staff = models.BooleanField()
#     is_bod = models.BooleanField()

# class User(AbstractUser):
#     ROLES = (
#         (1, 'student'),
#         (2, 'teacher'),
#         (2, 'staff'),
#     )

#     role = models.SmallIntegerField(choices=ROLES)

class Role(models.Model):
    ROLES = (
        (1, 'visiter'),
        (2, 'auditor'),
        (3, 'journalist'),
        (4, 'admin'),
    )

    id = models.SmallIntegerField(choices=ROLES, primary_key=True)

    def __str__(self) -> str:
        return self.get_id_display()

class User(AbstractUser):
    role = models.ManyToManyField(Role)
    address = models.CharField(max_length=200, blank=True)
    email_validator = EmailValidator()
    # email = models.CharField(
    #     _('email'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[email_validator],
    #     error_messages={
    #         'unique': _("A user with that email already exists."),
    #     },
    # )

 