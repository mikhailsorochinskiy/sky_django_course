from django import forms
from .models import Product
from django.core.exceptions import ValidationError


exclude_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


def price_less_zero(price):
    if price < 0:
        raise ValidationError('Цена не может быть отрицательной')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','description', 'image', 'price']

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        price_less_zero(price)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in exclude_words:
            if word in name.lower():
                raise ValidationError('Название товара содержит запрещенные слова')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in exclude_words:
            if word in description.lower():
                raise ValidationError('Описание товара содержит запрещенные слова')
        return description
