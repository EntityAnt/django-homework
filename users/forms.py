from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField

from users.models import User
from django.core.validators import ValidationError


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'



class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'avatar',)

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
