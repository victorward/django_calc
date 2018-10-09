from django.db import models
from django.utils import timezone
import datetime


class Calculations(models.Model):
    timestamp = models.DateTimeField('creation time')
    operand1 = models.CharField(max_length=15)
    operator = models.CharField(max_length=1)
    operand2 = models.CharField(max_length=15)
    # result = models.CharField(max_length=15)

    def was_add_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.operand1 + " " + self.operator + " " + self.operand2

    # return self.timestamp + self.operand1 + self.operator + self.operand2 + self.result

