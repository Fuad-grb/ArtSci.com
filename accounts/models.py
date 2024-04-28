from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="users/%Y/%m/%d", default="users/user.png")
	bio = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=35, null=True)
	linkedin = models.URLField(null=True)
	facebook = models.URLField(null=True)
	instagram = models.URLField(null=True)
	github = models.URLField(null=True)

	def __str__(self):
		return self.user.username
