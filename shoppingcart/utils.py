def calculate_cart_total(shoppingcart, movies_in_cart):
    total = 0
    for movie in movies_in_cart:
        quantity = shoppingcart[str(movie.id)]
        total += movie.price * int(quantity)
    return total