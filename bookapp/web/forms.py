from django import forms

from bookapp.web.models import Profile, Book


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, item) in self.fields.items():
            item.widget.attrs['disabled'] = 'disabled'
