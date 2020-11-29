from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	contact = models.IntegerField(null=True)
	net_sgpi = models.DecimalField(max_digits = 4,null=True,decimal_places = 2) 
	address = models.CharField(max_length = 100,null=True) 
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,**kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Elective(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	elective = models.CharField(max_length = 100,null=True)
	semester = models.IntegerField(default='6')
	approved = models.BooleanField(default='False')

	def __str__(self):
		return f'{self.user}'

	class Meta:
		unique_together = (("user", "elective","semester"),)

