from django.db import models
from config import settings


class Slider(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Slider/', max_length=600)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class BigMenu(models.Model):
    title = models.CharField(max_length=255)
    icon_img = models.ImageField(upload_to='icon/', max_length=600)
    img = models.ImageField(upload_to='bigmenu/', max_length=600)

    def __str__(self):
        return self.title


class SmallMenu(models.Model):
    bigMenu = models.ForeignKey(BigMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='smallmenu/', max_length=600)

    def __str__(self):
        return self.title


class Product(models.Model):
    smallMenu = models.ForeignKey(SmallMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/', max_length=600)

    def __str__(self):
        return self.title


class NewProduct(models.Model):
    smallMenu = models.ForeignKey(SmallMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='newfoods/', max_length=600)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    old_price = models.IntegerField(blank=True, null=True)
    is_new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Aksiya(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='aksiya/', max_length=600)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Tables(models.Model):
    number = models.IntegerField(unique=True)  # Stol raqami
    stoldagi_orindiq_soni = models.IntegerField()
    is_aviable = models.BooleanField(default=True)

    def __str__(self):
        return f"Stol #{self.number} ({self.stoldagi_orindiq_soni} o'rindiq)"


class Order(models.Model):
    ismi = models.CharField(max_length=100)
    fmiliasi = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)  # Stolga bog'lanish
    buyurma_sanasi = models.DateTimeField()
    mehmonlar_soni = models.PositiveIntegerField()
    maxsus_sorovlar = models.TextField(blank=True, null=True)  # Maxsus so'rovlar

    def __str__(self):
        return f"{self.ismi} {self.fmiliasi} - {self.buyurma_sanasi}"
# class YetkazibBerish(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
