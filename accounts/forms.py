from dataclasses import field
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
