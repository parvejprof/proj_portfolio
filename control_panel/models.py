from django.db import models

# Create your models here.

class Import(models.Model):
        name = models.CharField(max_length=100)
        jobfile = models.FileField(upload_to='uploads/',blank=True)

        def __str__(self): return str(self.id)


from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return str(self.id)

    