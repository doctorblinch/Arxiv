# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Author(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField()

class Article(models.Model):
	header = models.CharField(max_length = 200)
	body_text = models.CharField(max_length = 10000)
	authors = models.ManyToManyField(Author)
	def __str__(self):
        	return self.header

# Create your models here.
