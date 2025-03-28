# basic models were created
This project is a Django-based Inventory Management System designed to manage categories, items, sizes, suppliers, customers, price history, orders, and user statuses.

# Features

- **Category Management**: Create and manage product categories.
- **Item Management**: Add items with descriptions, base prices, and associated categories.
- **Size Management**: Define various sizes for the items.
- **Supplier Management**: Keep track of suppliers and their contact information.
- **Customer Management**: Manage customer details for order processing.
- **Price History**: Track price changes for items over time.
- **Order Processing**: Place orders with automatic retrieval of the latest prices.
- **User Management**: Manage user statuses for different operations.

# each model use
The application consists of the following models:

- **Category**: Represents a category of items.
  - `category_name`: Name of the category.
  - `description`: Description of the category.

- **Item**: Represents an item in the inventory.
  - `item_name`: Name of the item.
  - `description`: Detailed description of the item.
  - `base_price`: Base price of the item.
  - `category`: Foreign key to the `Category` model.

- **Size**: Represents sizes for items.
  - `size_name`: Name of the size.
  - `symbol`: Symbol representing the size.
  - `description`: Description of the size.

- **Supplier**: Represents suppliers of items.
  - `company_name`: Name of the supplier company.
  - `contact_person`: Name of the contact person at the supplier.
  - `phone_number`: Contact phone number.
  - `email`: Contact email.

- **Customer**: Represents customers placing orders.
  - `full_name`: Full name of the customer.
  - `phone_number`: Customer's phone number.
  - `email`: Customer's email address.

- **PriceHistory**: Records the price history of items.
  - `item`: Foreign key to the `Item` model.
  - `size`: Foreign key to the `Size` model.
  - `price`: Price of the item.
  - `effective_date`: Date the price became effective.

- **IncomingItem**: Represents incoming stock for items.
  - `item`: Foreign key to the `Item` model.
  - `size`: Foreign key to the `Size` model.
  - `quantity_received`: Quantity of items received.
  - `date_received`: Date of receipt.
  - `supplier`: Foreign key to the `Supplier` model.

- **Order**: Represents customer orders.
  - `order_id`: Unique identifier for the order.
  - `item`: Foreign key to the `Item` model.
  - `size`: Foreign key to the `Size` model.
  - `customer`: Foreign key to the `Customer` model.
  - `quantity`: Quantity of items ordered.
  - `price`: Current price from `PriceHistory`.
  - `status`: Current status of the order.

- **Status**: Represents different statuses for users.
  - `status_name`: Name of the status.
  - `description`: Description of the status.

- **User**: Represents application users.
  - `user_name`: Unique username.
  - `status`: Foreign key to the `Status` model.