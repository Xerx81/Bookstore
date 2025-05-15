from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review"]
        widgets = {
            "review": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Write your review here..."
            }),
        }
