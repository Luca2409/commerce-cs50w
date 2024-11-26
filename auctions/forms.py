from django import forms

class CreateListing(forms.Form):
    title = forms.CharField(label="title", max_length=64)
    description = forms.CharField(label="description", widget=forms.Textarea)
    category = forms.CharField(label="category", max_length=64)
    picture = forms.URLField(label="picture")
    bid_height = forms.IntegerField(label="bid_height")

class SubmitBid(forms.Form):
    bid = forms.IntegerField(label="bid")

class CommentForm(forms.Form):
    title = forms.CharField(label="title", max_length=64)
    text = forms.CharField(label="text", max_length=300)
