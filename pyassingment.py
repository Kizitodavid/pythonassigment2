class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name  # Name of the product
        self.price = price                  # Price of the product
        self.quantity_in_stock = quantity_in_stock  # Quantity available in stock

    def display_product_info(self):
        #"""Displays the product details."""
        return f"Product: {self.product_name}, Price: ${self.price:.2f}, Available: {self.quantity_in_stock}"

class ShoppingCart:
    total_carts = 0  # Class variable to track total number of shopping carts

    def __init__(self):
        self.items = []  # List to hold items in the cart
        ShoppingCart.total_carts += 1  # Increment the cart count when a new cart is created

    def add_to_cart(self, product, quantity):
        #"""Adds a product to the cart if the quantity is available."""
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Decrease the stock
        else:
            print(f"Cannot add {quantity} of {product.product_name}. Not enough stock.")

    def remove_from_cart(self, product):
        #"""Removes a product from the cart."""
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Increase stock since item is removed
                break

    def display_cart(self):
        #"""Displays all items in the cart."""
        if not self.items:
            return "Cart is empty."
        cart_details = []
        for product, quantity in self.items:
            cart_details.append(f"{product.product_name} x {quantity}")
        return "\n".join(cart_details)

    def calculate_total(self):
        #"""Calculates and returns the total price of items in the cart."""
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

# Example usage

# Creating Product instances
product1 = Product("Laptop", 999.99, 10)
product2 = Product("Mouse", 25.99, 100)
product3 = Product("Keyboard", 49.99, 50)

# Creating ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding products to cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)

# Adding products to cart2
cart2.add_to_cart(product3, 1)
cart2.add_to_cart(product1, 1)  # Trying to add again to test stock reduction

# Displaying cart contents and total for cart1
print("Cart 1 Items:")
print(cart1.display_cart())
print(f"Total for Cart 1: shs{cart1.calculate_total():.2f}\n")

# Displaying cart contents and total for cart2
print("Cart 2 Items:")
print(cart2.display_cart())
print(f"Total for Cart 2: shs{cart2.calculate_total():.2f}\n")

# Attempting to remove an item
cart1.remove_from_cart(product2)
print("Cart 1 Items after removing Mouse:")
print(cart1.display_cart())
print(f"Total for Cart 1 after removal: ${cart1.calculate_total():.2f}")
