from django.db import models

class Announcements(models.Model):
	title = models.CharField(max_length=100,verbose_name = "Title")
	file = models.FileField(upload_to='uploads/%Y %m %d/',blank=True)

	def __str__(self):
		return f'{self.title}'
		
	class Meta:
		verbose_name_plural = "Announcements"

