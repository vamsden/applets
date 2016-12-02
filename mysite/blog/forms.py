from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField(label='Sender ID')
	to = forms.EmailField(label='Receiver ID')
	comments = forms.CharField(required=False, widget=forms.Textarea(
		attrs={
			# Form attributes also check label field above.
			"id": "comments",
			"title": "Insert Comments",
			"placeholder": "Place your comments here",
		})
	)


# Comment Model Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        # Optional Field Widgets
        """widgets = {
			'text': forms.TextInput(
                attrs={
                	'id': 'post-text',
                	'required': True, 
                	'placeholder': 
                	'Say something...'
        }"""
