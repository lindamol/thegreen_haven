from django.db import models


# ======================
# CUSTOMER TABLE
# ======================
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ======================
# PLANT TABLE
# ======================
class Plant(models.Model):
    slug = models.SlugField(unique=True, default="")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    size = models.CharField(max_length=50, default="")
    stock = models.CharField(max_length=50, default="In Stock")

    image = models.CharField(max_length=200, blank=True)

    description = models.TextField(default="")
    care_instructions = models.TextField(default="")

    def __str__(self):
        return self.name


# ======================
# CART TABLE
# ======================
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.customer.name}"


# ======================
# CART ITEM TABLE
# ======================
class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.plant.name} x {self.quantity}"