from django import forms
from livros.models import Livro
from utils.django_forms import add_attr
from utils.strings import is_positive_number
from django.core.exceptions import ValidationError
from collections import defaultdict

class AuthorlivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        
        add_attr(self.fields.get('total_de_paginas'), 'class', 'span-2')
        
    class Meta:
        model = Livro
        fields = 'titulo', 'descricao1', 'descricao2', \
            'total_de_paginas', 'capa'
        widgets = {
            'capa': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
        }
        
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        titulo = cd.get('titulo')
        descricao1 = cd.get('descricao1')

        if titulo == descricao1:
            self._my_errors['titulo'].append('Cannot be equal to descricao1')
            self._my_errors['descricao1'].append('Cannot be equal to titulo')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')

        if len(titulo) < 5:
            self._my_errors['titulo'].append('Must have at least 5 chars.')

        return titulo

    def clean_preparation_time(self):
        field_name = 'total_de_paginas'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Must be a positive number')

        return field_value