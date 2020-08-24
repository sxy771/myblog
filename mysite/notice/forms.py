# notice/forms.py

from django import forms
from .models import Notice

class NoticeWriteForm(forms.ModelForm):
    # files = forms.FileField(widget=forms.ClearableFileInput(attrs={
    #     'multiple': True
    #     }))
    def __init__(self, *args, **kwargs):
        super(NoticeWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'title'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please enter the title.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })

    class Meta:
        model = Notice
        fields = ['title', 'content', 'upload_files', 'top_fixed']