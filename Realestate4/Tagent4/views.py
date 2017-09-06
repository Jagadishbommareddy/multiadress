from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Agent
from .forms import AddressFormSet


class AgentList(ListView):
    model = Agent


class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes']


class AgentAddressCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddressCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST)
        else:
            data['address'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(AgentAddressCreate, self).form_valid(form)


class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes']


class AgentAddressUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddressUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            data['address'] = AddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(AgentAddressUpdate, self).form_valid(form)


class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')
