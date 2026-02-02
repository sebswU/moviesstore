from django import template
register = template.Library()
@register.filter(name='get_quantity')
def get_cart_quantity(shoppingcart, movie_id):
    return shoppingcart[str(movie_id)] 