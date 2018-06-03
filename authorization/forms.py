from django import forms
from django.forms import ModelForm
from authorization.models import Authorization

class Auth_Create(ModelForm):

	class Meta:
		model=Authorization
		fields=['authorizationid','memberid','ndc_no','startdate','enddate']