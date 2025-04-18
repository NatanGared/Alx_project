from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.item_name

class Size(models.Model):
    size_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.size_name

class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.company_name
    
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class PriceHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='price_history_item')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='price_history_size')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()

    def __str__(self):
        return f"{self.price} on {self.effective_date}"

class IncomingItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='incoming_items')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='incoming_items_size')
    quantity_received = models.PositiveIntegerField()
    date_received = models.DateField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name='supplier')

    def __str__(self):
        return f"{self.quantity_received}"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders_item')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='orders_item_size')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders_customer')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_id} by {self.customer}"
