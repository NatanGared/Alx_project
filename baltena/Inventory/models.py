from django.db import models

class Category(models.Model):
    category_name = models.Charfield(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Item(models.Model):
    item_name = models.Charfield(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.description

class PriceHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()

    def __str__(self):
        return f"{self.item.description} - {self.price} on {self.effective_date}"


class IncomingItems(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='incoming_items')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='incoming_items')
    quantity_received = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity_received} of {self.item.description}"


class Size(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order {self.order_id} by {self.customer}"


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Supplier(models.Model):
    full_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name


class Status(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='users')
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username