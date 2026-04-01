from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plant(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField(default="No description available")
    care_instructions = models.TextField(default="No care instructions available")

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ NEW FIELDS (ADDED)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"Cart {self.id} - {self.customer.name}"


class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'plant')  # ✅ composite key

    def __str__(self):
        return f"{self.cart} - {self.plant} ({self.quantity})"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Completed')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"