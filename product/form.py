# import email
# from turtle import title, width
from django import forms
from .models import product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "your title"})) #if you want the label to not even appear,make it empty string
    email = forms.EmailField()
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new_class-name two",
                "placeholder": "your description",
                "id": "my-id-for-textarea",
                "rows" : 20,
                "cols":120
            }))
    price = forms.DecimalField(initial=99.99) 
    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs): #clean_<my_field_name> 
        title= self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title")
        return title
        
    # def clean_email(self,*args,**kwargs): #clean_<my_field_name> 
    #     email = self.cleaned_data.get("title")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("this is not a valid email")
    #     return email

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"})) #if you want the label to not even appear,make it empty string
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new_class-name two",
                "placeholder": "your description",
                "id": "my-id-for-textarea",
                "rows" : 20,
                "cols":120
            }))
    price = forms.DecimalField(initial=99.99) 