from django.db import models

subclass = (
    ("Dermatology", "Dermatologist"),
    ("neurology", "Neurologist"),
    ("surgeon", "surgeon"),
    ("cardiology", "cardiologist"),
    ("General_surgery", "General_surgery"),
)


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    Doctor_field = models.CharField(max_length=100, choices=subclass, default='General_surgery')
    Checkup_on = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Snippet'
