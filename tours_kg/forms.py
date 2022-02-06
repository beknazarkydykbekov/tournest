from django import forms
from tours_kg.models import BookNow, Review, JoinUs
from tours_kg.models import BookNow, Review, User


class BookNowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookNowForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    # sightseeing = forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите Тур'},
    # choices=BookNow.sightseeing)

    class Meta:
        model = BookNow
        fields = ('__all__')


class JoinUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JoinUsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JoinUs
        fields = ('__all__')





class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = (
            'name', 'reviews'
        )
