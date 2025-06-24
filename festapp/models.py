from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    id_card = models.FileField(upload_to='id_cards/')
    payment_status = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
