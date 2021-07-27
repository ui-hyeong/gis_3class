from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):

    class Meta:  #
        model = Profile
        fields = ['image', 'nickname', 'message']  # 모델에서 어떤걸 받을건지

