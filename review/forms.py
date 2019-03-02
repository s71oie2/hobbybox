from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # label의 : 안 보이게
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('product', 'title', 'text', 'rating')

    product = forms.CharField(label='취미', widget=forms.TextInput(
        attrs={
            'class': 'review_prod'
        }
    ))

    title = forms.CharField(label='제목', widget=forms.TextInput(
        attrs={
            'class': 'review_title'
        }
    ))

    text = forms.CharField(label='본문', widget=forms.TextInput(
        attrs={
            'class': 'review_text'
        }
    ))

    rating = forms.CharField(label='평점', widget=forms.TextInput(
        attrs={
            'class': 'review_rate',
            'placeholder': '☆☆☆☆☆'
        }
    ))
