price = float(input("Price = "))
discount = float(input("Discount = "))
discount_of = price * (discount/100)
price_after = price - discount_of
print(f'Price with discount: {price_after}')
print(f'Reduction: {discount_of}')