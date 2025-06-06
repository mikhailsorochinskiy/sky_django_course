import os

from django import forms
from .models import Product
from django.core.exceptions import ValidationError


exclude_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


def validate_image(image):
    # Проверяем размер (5MB = 5 * 1024 * 1024 байт)
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Размер изображения не должен превышать 5MB.")

    # Проверяем формат (только JPEG и PNG)
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Допустимые форматы изображений: JPEG, PNG.")


def price_less_zero(price):
    if price < 0:
        raise ValidationError('Цена не может быть отрицательной')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','description', 'image', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара'
        })



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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_image(image)
        return image

class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','description', 'image', 'price', 'is_active']

    def __init__(self, *args, **kwargs):
        super(ProductModeratorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара'
        })

        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check'
        })

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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_image(image)
        return image
