from django import forms

from .models import Post,PostDetail,Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "content"
 ]

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Entry')
    class Meta:
        model = Comment
        fields = [
            "text",
            "author"

 ]


