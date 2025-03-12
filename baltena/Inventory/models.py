from django.db import models

class Item(models.Models):      # for inserting item name and description
    name = varcharfield(max_limit = 100)
    description = textfield()
    pass

class Size(models.Models):      # for inserting the different sizes of the item is prepared or sold
    pass

class Price(models.Models):     # for the price of different items at different times
    pass

class Amount(models.Models):        # for registering and controlling the amount of items available at any given time
    pass

class Incoming(models.Models):      # for inserting newly prepared items
    pass

class Sales(models.Models):     # for registering sold items
    pass

class Customer(models.Models):      # for registering the name of the buyers
    name
    gender
    email
    pass