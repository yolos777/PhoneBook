from django import forms
from . import models

# создаем форму для добавления новых контактов
class AddContact(forms.ModelForm):

    # определяем параметр phone, так как у нас нет соответствующего поля в классе Names
    phone = forms.CharField(widget = forms.TextInput())
    class Meta:
        model = models.Names
        fields = (
            'name',
            'surname',
            'phone'
        )