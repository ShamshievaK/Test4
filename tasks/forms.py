from django import forms
from .models import Category, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']

class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категория')
    title = forms.CharField(max_length=200, required=False, label='Поиск по категории')


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите текст для поиска",
                "class": "form-control",
            }
        )
    )

