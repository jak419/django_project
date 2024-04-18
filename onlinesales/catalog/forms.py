from django import forms
from .models import Orders, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['product', 'order_quantity', 'unit_price', 'extended_amount','currency', 'customer', 'order_date_actual', 'due_date_actual', 'ship_date_actual', 'sales_order_line_number']
        widgets = {
            'order_date_actual': forms.DateInput(attrs={'type': 'date'}),
            'due_date_actual': forms.DateInput(attrs={'type': 'date'}),
            'ship_date_actual': forms.DateInput(attrs={'type': 'date'}),
            'unit_price': forms.TextInput(attrs={'readonly': True}),
            'extended_amount': forms.TextInput(attrs={'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        
        self.fields['product'].queryset = Product.objects.all()
        self.fields['product'].label_from_instance = lambda obj: f"{obj.english_product_name} (ID: {obj.id})"

        self.fields['product'].help_text = "Select a product by its ID and name"

    def save(self, commit=True):
        instance = super(OrderForm, self).save(commit=False)
        # IF 'unit_price' and 'order_quantity' are already validated as numbers:
        instance.extended_amount = instance.order_quantity * instance.unit_price
        if commit:
            instance.save()
        return instance
    
