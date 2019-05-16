from django import forms


class ThreadForm(forms.Form):
    title_max = 30
    title=forms.CharField(
        label='Title of thread',
        max_length=title_max,
        required=True,
        help_text='Required, maximum of {} characters'.format(title_max)
    )

    header_max=80
    header = forms.CharField(
        label='Header of content',
        max_length=header_max,
        required=True,
        help_text='Required, maximum of {} characters'.format(header_max)
    )

    text = forms.CharField(
        widget=forms.Textarea,
        label='Content',
        required=True,
        help_text='Required'
    )

    image = forms.ImageField(
        label='Image',
        help_text="NOTE: You can only add one picture! "
                  "Post images with caution, WebForum is not responsible for misuse of your content"
    )
