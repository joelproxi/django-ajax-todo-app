from django.db import models

# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.description[:20]
    
    class Meta:
        ordering = ('-created_at',)
        indexes = [models.Index(fields=['created_at'])]