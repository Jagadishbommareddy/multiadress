from django.forms import ModelForm, inlineformset_factory

from .models import Agent, Address


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()


AddressFormSet = inlineformset_factory(Agent, Address,
                                            form=AddressForm, extra=1)
