# -*- encoding: utf-8 -*-

# django
from django import forms

# project
from guest.models import *


class AddPictureForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AddPictureForm, self).__init__(*args, **kwargs)

		self.fields['picture_data'] = forms.ImageField()

	class Meta:
		model = Picture
		exclude = ('name', 'thumbnail_data')
