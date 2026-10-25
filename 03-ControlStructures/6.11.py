current_product_price= int(input('whats the current product price: '))
previous_product_price= int(input('what the previous proiduct price: '))
if current_product_price <= 0.9*(previous_product_price):
    print("it workds")
else:
    print('it odesnt work')