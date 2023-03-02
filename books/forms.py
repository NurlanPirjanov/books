from django import forms
from .models import *

inputClass = 'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
selectClass = 'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
datetimeClass = 'shadow-sm my-2 max-w-sm bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': inputClass}),
            'lang': forms.Select(attrs={'class':selectClass}),
            'year': forms.DateTimeInput(attrs={'type': 'date', 'class': datetimeClass}),
            'book_author': forms.TextInput(attrs={'class': inputClass}),
            'isbn': forms.TextInput(attrs={'class': inputClass}),
            'printing_office': forms.TextInput(attrs={'class': inputClass}),
            'science': forms.TextInput(attrs={'class': inputClass}),
            'teacher': forms.TextInput(attrs={'class': inputClass}),
            'book_number': forms.TextInput(attrs={'type': 'number', 'class': inputClass}),
            'book_url_file': forms.TextInput(attrs={
                'type': 'url',
                'placeholder': 'https://example.com/abc',
                'class': 'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 '
                         'focus:border-blue-500 block w-full p-2.5'}),
            'kurs': forms.Select(attrs={'class': selectClass}),
            'sem': forms.Select(attrs={'class': selectClass}),
            'yunalish': forms.Select(attrs={'class': selectClass}),
            'kafedra': forms.Select(attrs={'class': selectClass}),
        }
        labels = {
            'sem': 'Semestr',
            'book_name': 'Kitob nomi',
            'lang': 'Til',
            'year': 'Nashr yili',
            'yunalish': 'Yo\'nalish',
        }