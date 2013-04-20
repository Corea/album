from django.db import models

import os

# Create your models here.

class Album(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=63)
	created_datetime = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'[%s] %s' % (self.id, self.name)

class Picture(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=127)
	picture_data = models.ImageField(upload_to=\
		os.path.join(os.path.dirname(__file__), '../upload/picture/'))
	thumbnail_data = models.ImageField(upload_to=\
		os.path.join(os.path.dirname(__file__), '../upload/thumbnail/'), editable=False)
	created_datetime = models.DateTimeField(auto_now_add=True)

	def make_thumbnail(self):
		from PIL import Image
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile

        # open original photo which we want to thumbnail using pil's image
        # object
		print self.picture_data
		image = Image.open(self.picture_data.name)

        # convert to rgb if necessary
        # thanks to limodou on djangosnippets.org
        # http://www.djangosnippets.org/snippets/20/
		if image.mode not in ('L', 'RGB'):
			image = image.convert('RGB')

        # we use our pil image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # additionally, we use image.antialias to make the image look better.
        # without antialiasing the image pattern artifacts may result.
		image.thumbnail((128, 128), Image.ANTIALIAS)

        # save the thumbnail
		temp_handle = StringIO()
		image.save(temp_handle, 'png')
		temp_handle.seek(0)

        # save to the thumbnail field
		suf = SimpleUploadedFile(os.path.split(self.picture_data.name)[-1],
			temp_handle.read(), content_type='image/png')
		self.thumbnail_data.save(suf.name, suf, save=True)
		self.name = self.picture_data.name.split('/')[-1]
		self.save()



	def __unicode__(self):
		return u'[%s] %s' % (self.id, self.picture_data)
	
