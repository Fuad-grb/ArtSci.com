from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

	STATUS_TYPE =(
		('publish', 'Publish'),
		('draft', 'Draft')

		)

	title = models.CharField(max_length = 120)
	description = models.CharField(max_length=120)
	content = models.TextField(null = True)
	image = models.ImageField(upload_to="images/posts/%Y/%m/%d")
	created_at = models.DateTimeField(auto_now_add=True)
	preview = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	slug = models.SlugField()
	status = models.CharField(max_length=30, choices=STATUS_TYPE, default='draft')

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment
