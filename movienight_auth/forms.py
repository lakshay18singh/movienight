from django_registration.forms import RegistrationForm as DefaultRegistrationForm
from django.contrib.auth import get_user_model
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

User = get_user_model()
class RegistrationForm(DefaultRegistrationForm):
    
    class Meta(DefaultRegistrationForm.Meta):
      model=User
      

    def __init__(self, *args, **kwargs):
      super(RegistrationForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.add_input(Submit('submit', 'Submit'))
    
      