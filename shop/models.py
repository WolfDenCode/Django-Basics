from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # Add SlugField
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Add UUIDField

    def save(self, *args, **kwargs):
        # Automatically generate a slug if it doesn't exist
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")  # Simple slug generation
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name    


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="detail")
    manufacturer = models.CharField(max_length=100)
    warranty_period = models.IntegerField(help_text="Warranty period in months")
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details for {self.product.name}"
    

    