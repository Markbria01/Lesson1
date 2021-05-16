import abc


def discounted(price, discount, max_distcoun = 50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_distcoun = abs(float(max_distcoun))
    if discount > 99:
        raise ValueError('Максиммальная скидка не более 99%')
    if discount >= max_distcoun:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


print(discounted(100, 40))