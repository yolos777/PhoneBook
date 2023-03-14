from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms
from . import models



class BookOfContacts(TemplateView):
    template_name = 'Main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        tip = 'All contacts'
        if search_by == 'surname' and query:
            tip = f"Filtered by {query}"
            contact_cards = models.Names.objects.filter(surname = query)
            context['tip'] = tip
            context['contact_cards'] = contact_cards
            return context
        context['tip'] = tip
        context["contact_cards"] = models.Names.objects.all()
        return context

class NewContact(CreateView):
    template_name = 'NewContact.html'
    form_class = forms.AddContact
    success_url = reverse_lazy('home')

    def get_success_url(self):
        phone_number = self.request.POST.get('phone')
        for num in phone_number.split('\n'):
            models.Contacts.objects.create(phone_number = num, contact = self.object)
        return super().get_success_url()

class DeleteContact(DeleteView):
    model = models.Names
    template_name = 'Goodbye.html'
    success_url = reverse_lazy('home')