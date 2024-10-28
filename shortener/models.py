from django.db import models
import string, random

def generate_shortcode():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, default=generate_shortcode)
    access_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.short_code} -> {self.url}"
