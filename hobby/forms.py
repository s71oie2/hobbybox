from django import forms

class SearchForm(forms.Form):
    search_word = forms.CharField(label='검색어', required=False)