from django import forms


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField(label='Sender ID')
	to = forms.EmailField(label='Receiver ID')
	comments = forms.CharField(required=False, widget=forms.Textarea(
		attrs={
			"id": "comments",
			"title": "Insert Comments",
			"placeholder": "Place your comments here",
		})
	)