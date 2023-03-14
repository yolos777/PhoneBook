from django import forms
from . import models

# ������� ����� ��� ���������� ����� ���������
class AddContact(forms.ModelForm):

    # ���������� �������� phone, ��� ��� � ��� ��� ���������������� ���� � ������ Names
    phone = forms.CharField(widget = forms.TextInput())
    class Meta:
        model = models.Names
        fields = (
            'name',
            'surname',
            'phone'
        )