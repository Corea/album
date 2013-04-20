# -*- encoding: utf-8 -*-

# django
from django.core.context_processors import csrf
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext

# 3rd Party
from PIL import Image

# project
from guest.models import *
from guest.forms import *


def list_picture(request):
	pictures = Picture.objects.all()
	variables = RequestContext(request, {
		'pictures': pictures
	})
	return render_to_response('guest/list.html', variables)

def add_picture(request):
	if request.method == 'POST':
		form = AddPictureForm(request.POST, request.FILES, label_suffix='')
		if form.is_valid():
			data = form.clean()

			picture = Picture.objects.create(
				picture_data=data['picture_data'],
			)
			picture.make_thumbnail()
	else:
		form = AddPictureForm(label_suffix='')

	variables = RequestContext(request, {
		'form': form,
	})
	return render_to_response('guest/add.html', variables)
