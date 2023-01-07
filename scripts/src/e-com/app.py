import pydispatch

# Create an event for placing an order
order_placed = pydispatch.Signal()

# Create a handler function for the order placed event
def handle_order_placed(sender, **kwargs):
    # Update the inventory
    update_inventory(kwargs["product_id"], kwargs["quantity"])
    
    # Calculate the shipping cost
    shipping_cost = calculate_shipping_cost(kwargs["shipping_address"])
    
    # Charge the customer's credit card
    charge_credit_card(kwargs["credit_card"], kwargs["total_amount"])

# Connect the event to the handler function
order_placed.connect(handle_order_placed)

# Place an order
order_details = {
    "product_id": 123,
    "quantity": 2,
    "shipping_address": "123 Main St",
    "credit_card": "1234567890",
    "total_amount": 100.00
}
order_placed.send(order_details)
