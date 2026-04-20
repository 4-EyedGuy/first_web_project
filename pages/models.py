from django.db import models
from django.urls import reverse

class Plugin(models.Model):
    image = models.ImageField(upload_to='plugins/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugin_detail', args=[self.pk])
    
    class Meta:
        ordering = ['-created_at']