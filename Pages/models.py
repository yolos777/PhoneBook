from django.db import models

# ƒл€ нашего простенького телефонного справочника достаточно всего двух класов - им€ и контакт
class Names(models.Model):
    name = models.CharField("Contact name", max_length = 50)
    surname = models.CharField("Contact surname", max_length = 50)

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_phone_numbers(self):
        return "".join([phone.phone_number for phone in self.phone.all()])

class Contacts(models.Model):
    phone_number = models.CharField("Phone number", max_length = 50)
    contact = models.ForeignKey(Names, on_delete = models.CASCADE, related_name = 'phone')

    def __str__(self):
        return self.phone_number