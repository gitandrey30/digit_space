from django import forms

from .models import VWCar, ModelOfCar, DieselEngine


class NewCarForm(forms.ModelForm):
    class Meta:
        model = VWCar
        fields = "__all__"


class NewModelForm(forms.ModelForm):
    class Meta:
        model = ModelOfCar
        fields = "__all__"


class NewEngineForm(forms.ModelForm):
    class Meta:
        model = DieselEngine
        fields = '__all__'

class ChooseCarForm(forms.Form):
    manufacturer = forms.ModelChoiceField(queryset = VWCar.objects.all())
    model_of_car = forms.ModelChoiceField(queryset = ModelOfCar.objects.all())