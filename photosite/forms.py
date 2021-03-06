from .models import Category
from django import forms

class CategorySelectionForm(forms.Form):
    """
    A form to enable the filtering of photos by category
    """
    category_list = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                           empty_label="All categories",
                                           widget=forms.Select(attrs={"onChange":'this.form.submit()'}))
    category_list.label = ''
    category_list.required=False