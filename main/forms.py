from django.forms import ModelForm
from main.models import NewJersey

class JerseyForm(ModelForm):
    class Meta:
        model = NewJersey
        fields = ["name", "price", "description", "image", "quantity"]