from django.db import models

class Category(models.Model):
    name = models.CharField("Nom de la catégorie", max_length=100)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["name"]

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField("Nom du plat", max_length=100)
    description = models.TextField("Description")
    price = models.DecimalField("Prix (DT)", max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    image = models.ImageField("Image du plat", upload_to='menu_images/', blank=True, null=True)

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name