from django import forms
from user.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "User",
            "Title",
            "Text",
            "Image",
        ]
