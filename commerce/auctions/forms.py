from django import forms
from .models import AuctionListing

class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'price', 'starting_bid', 'category', 'image','end_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-group', 'placeholder': 'Give it a title'}),

            'description': forms.Textarea(attrs={'class': 'form-control form-group', 'placeholder': 'Tell more about the product', 'rows': '3'}),

            'price': forms.NumberInput(attrs={'class': 'form-control form-group', 'placeholder': 'Estimated price (optional)', 'min': '0.01', 'max': '999999999.99', 'step': '0.01'}),

            'starting_bid': forms.NumberInput(attrs={'class': 'form-control form-group', 'placeholder': 'Starting bid', 'min': '10', 'max': '99999999999.99', 'step': '10'}),

            'category': forms.TextInput(attrs={'class': 'form-control form-group', 'autocomplete': 'on', 'placeholder': 'Category (optional)'}),

            'image': forms.FileInput(attrs={'class': 'form-control form-group', 'accept': 'image/*'}),

            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})

        }

    def clean_starting_bid(self):
        amount = float(self.cleaned_data.get('starting_bid'))
        if isinstance(amount, float) and amount > 0:
            return amount
        print(amount)
        raise forms.ValidationError('Should be a number larger than zero!')

    def clean_category(self):
        category = self.cleaned_data.get('category')
        return category.lower()


class CommentForm(forms.Form):
    text = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control-md lead form-group',
            'rows': '3',
            'cols': '100'
        }
        )
    )

    def clean_comment(self):
        text = self.cleaned_data.get('text')
        if len(text) > 0:
            return text
        return self.errors
