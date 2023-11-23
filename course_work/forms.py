from django import forms
from .models import Review, PaymentMethodChoices, DeliveryMethodChoices, Order


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer', 'rating', 'description']
        labels = {
            'customer': 'Покупатель',
            'rating': 'Рейтинг',
            'description': 'Коментарий'
        }
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'notes', 'used_promocode', 'payment_method', 'delivery_method', 'delivery_address']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'email': 'Почта',
            'notes': 'Комментарий',
            'used_promocode': 'Промокод',
            'payment_method': 'Способ оплаты',
            'delivery_method': 'Способ доставки',
            'delivery_address': 'Адрес доставки',
        }