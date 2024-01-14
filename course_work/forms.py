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

    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        if customer == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        return customer

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError("Рейтинг должен быть в диапазоне от 1 до 5.")
        return rating

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        if len(description) > 1000:
            raise forms.ValidationError("Количество символов не должно превышать 1000.")
        if len(description) < 10:
            raise forms.ValidationError("Количество символов должно быть не менее 10.")
        return description
        
from django import forms
from .models import Order

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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        if len(first_name) > 128:
            raise forms.ValidationError("Количество символов не должно превышать 128.")
        if len(first_name) < 2:
            raise forms.ValidationError("Количество символов должно быть не менее 2.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        if len(last_name) > 128:
            raise forms.ValidationError("Количество символов не должно превышать 128.")
        return last_name
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        if len(phone) > 16:
            raise forms.ValidationError("Количество символов не должно превышать 16.")
        if len(phone) < 6:
            raise forms.ValidationError("Количество символов должно быть не менее 6.")
        return phone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        if len(email) > 128:
            raise forms.ValidationError("Количество символов не должно превышать 128.")
        return email
    
    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        if len(notes) > 1000:
            raise forms.ValidationError("Количество символов не должно превышать 1000.")
        return notes
    

    
    def clean_payment_method(self):
        payment_method = self.cleaned_data.get('payment_method')
        if payment_method == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        return payment_method
    
    def clean_delivery_method(self):
        delivery_method = self.cleaned_data.get('delivery_method')
        if delivery_method == "":
            raise forms.ValidationError("Поле не может быть пустым.")
        return delivery_method
    
    def clean_delivery_address(self):
        delivery_address = self.cleaned_data.get('delivery_address')
        if len(delivery_address) > 1000:
            raise forms.ValidationError("Количество символов не должно превышать 1000.")
        return delivery_address
    

