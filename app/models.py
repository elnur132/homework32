from django.db import models

# Create your models here.
class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    
class TypeBody(models.Model):
    type_body_name = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'
        ordering = ['type_body_name']
        
    def __str__(self):
        return self.type_body_name