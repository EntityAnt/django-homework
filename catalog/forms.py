from django.forms import ModelForm, BooleanField

from catalog.models import Product, Category

from django.core.validators import ValidationError

BANNED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['views_counter', ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if any(word in name.lower() for word in BANNED_WORDS) or any(
                word in description.lower() for word in BANNED_WORDS):
            raise ValidationError('Извините, но в названии или описании товара нельзя использовать запрещенные слова.')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной!')
        return price

    def clean_photo(self):
        image = self.cleaned_data.get('photo')

        # Проверка формата файла
        if image:
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError("Формат файла должен быть JPEG или PNG.")

            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise ValidationError("Размер файла не должен превышать 5 МБ.")

        return image


class CategoryForm(FormStyleMixin, ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description')


