from django import forms
from backend.disease.models import Treatment, Prediction


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = "__all__"
