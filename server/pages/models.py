from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)

class ListItem(models.Model):
	id = models.AutoField(primary_key=True)
	list = models.ForeignKey(List, on_delete=models.CASCADE)
	text = models.CharField(max_length=255)