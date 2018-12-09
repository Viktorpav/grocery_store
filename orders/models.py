from django.db import models
from PIL import Image

class Menu_IceCream(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    image = models.ImageField(default='default.jpg', upload_to='MenuIceCream_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
