from django import forms

class CreateListing(forms.Form):
    title = forms.CharField(label="title", max_length=64)
    description = forms.CharField(label="description", widget=forms.Textarea)
    category = forms.CharField(label="category", max_length=64)
    picture = forms.URLField(label="picture")
    bid_height = forms.IntegerField(label="bid_height")