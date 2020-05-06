from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """This view renders the entire contents of the cart"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    messages.success(request, "Successfully added to cart")
    return redirect(request.META['HTTP_REFERER'])


def adjust_cart(request, id):
    """This allows the user to add or remove items from the cart"""

    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
