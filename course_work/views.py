from django.shortcuts import render, redirect
from course_work.models import Category, Item, OrderItem, Promocode, Article
from .forms import ReviewForm, OrderForm
from decimal import Decimal

def categories(request):
    categories = Category.objects.all()
    return render(request, 'catalog/categories.html', {'categories': categories})

def catalog(request, category):
    cat = Category.objects.get(slug=category)
    items = cat.item_set.all()
    return render(request, 'catalog/category.html', {'category': cat, 'items': items})

def item(request, item_id):
    i = Item.objects.get(id=item_id)
    reviews = i.review_set.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = i
            review.save()
            return redirect('item', item_id=item_id)
    else:
        form = ReviewForm()

    cart = request.session.get('cart', {})
    i.quantity = 0
    if str(item_id) in cart:
        i.quantity = cart[str(item_id)]

    return render(request, 'catalog/item.html', {'item': i, 'reviews': reviews, 'form': form})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('item', item_id=item_id)

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if cart[str(item_id)] > 0:
        cart[str(item_id)] -= 1
    request.session['cart'] = cart
    return redirect('item', item_id=item_id)

def view_cart(request):
    cart = request.session.get('cart', {})
    items = Item.objects.filter(id__in=map(int, cart.keys()))
    for item in items:
        item.quantity = cart[str(item.id)]
    total_payment_amount = sum(item.price * item.quantity for item in items)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            promocode_code = form.cleaned_data.get('used_promocode')
            total_payment_amount = sum(item.price * item.quantity for item in items)
            if promocode_code:
                promocode = Promocode.objects.get(code=promocode_code)
                if promocode.discount_percent:
                    discount = total_payment_amount * Decimal(str(promocode.discount_percent))
                elif promocode.discount_fixed:
                    discount = promocode.discount_fixed
                else:
                    discount = 0
                order.used_promocode = promocode.code
                order.payment_amount = total_payment_amount - discount
            else:
                order.payment_amount = total_payment_amount
            order.save()
            for item in items:
                order_item = OrderItem(order=order, item=item, quantity=item.quantity)
                order_item.save()
            return redirect('cart')
    return render(request, 'catalog/cart.html', {'items': items, 'cart': cart, 'form': form, 'total_payment_amount': total_payment_amount})




def remove_from_cart_in_cart(request, item_id):
    cart = request.session.get('cart', {})
    if cart[str(item_id)] > 1:
        cart[str(item_id)] -= 1
    else:
        del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('cart')

def add_to_cart_in_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def index(request):
    articles = Article.objects.all()
    return render(request, 'catalog/index.html', {'articles': articles})