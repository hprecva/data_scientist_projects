def update_shopping_cart(cart, action):
  product_id = action.get("product_id")

  if action["type"] == "add":
      if product_id in cart:
          cart[product_id] += action["quantity"]
      else:
          cart[product_id] = action["quantity"]

  elif action["type"] == "remove":
      cart[product_id] += 1

  elif action["type"] == "change" and action.get("quantity", 0) > 0:
      cart[product_id] = action["quantity"] - 1

  return cart

# do not modify the values below
print(update_shopping_cart({ "product_A": 4, "product_B": 3, "product_C": 1 }, { "type": "change", "product_id": "product_B", "quantity": 2 }))