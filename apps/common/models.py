from django.db import models

from apps.common import constants


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(estado=constants.STATUS_ACTIVATE)


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    status = models.IntegerField(choices=constants.STATUS_CHOICES, default=constants.STATUS_ACTIVATE)
    update_date = models.DateTimeField(auto_now=True, null=False)
    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        abstract = True

    def active(self):
        self.status = constants.STATUS_ACTIVATE
        self.save()

    def desactive(self):
        self.status = constants.STATUS_DEACTIVATE
        self.save()

    def is_deactivate(self):
        if self.status == constants.STATUS_DEACTIVATE:
            return True
        return False

    def is_activate(self):
        if self.status == constants.STATUS_ACTIVATE:
            return True
        return False
