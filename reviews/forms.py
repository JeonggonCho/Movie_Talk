from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    movie = forms.CharField(
        label='영화',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
            },
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
            },
        ),
    )
    
    class Meta:
        model = Review
        fields = ('title', 'movie', 'image', 'content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='Comment',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)