from django import forms


class FeedForm(forms.Form):
    name = forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Rating between 1-5'
            }
        )
    )

    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )
