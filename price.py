def discounted(price,discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount > 100:
        price_with_discount = price - price * discount / 100
        return price_with_discount

        
product = {'name': 'Samsung 10S', 'stock': 8, 'price': 50000.0, 'discount': 50}

product['with_discount'] = discounted(product['price'], product['discount'])

print(product)

discounted(100, 7)


