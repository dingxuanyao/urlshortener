from django.db.models import Model, URLField, CharField
import string
import random

# Create your models here.


class Url(Model):
    full_url = URLField(max_length=100)
    short_id = CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.id:
            chars = f"{string.ascii_letters}{string.digits}"
            self.short_id = ''.join(random.sample(chars, 5))
        return super().save(*args, **kwargs)
