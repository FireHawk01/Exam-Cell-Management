from django.db import models

class Announcements(models.Model):
	title = models.CharField(max_length=100,verbose_name = "Title")
	file = models.FileField(upload_to='uploads/%Y %m %d/',blank=True)

	def __str__(self):
		return f'{self.title}'
		
	class Meta:
		verbose_name_plural = "Announcements"


class Syllabus(models.Model):
	title = models.CharField(max_length=100,verbose_name = "Title")
	file = models.FileField(upload_to='uploads/%Y %m %d/',blank=True)

	def __str__(self):
		return f'{self.title}'
		
	class Meta:
		verbose_name_plural = "Syllabus"


class Calendar(models.Model):
	title = models.CharField(max_length=100,verbose_name = "Title")
	file = models.FileField(upload_to='uploads/%Y %m %d/',blank=True)

	def __str__(self):
		return f'{self.title}'
		
	class Meta:
		verbose_name_plural = "Academic Calendar and Holidays"

class Questionp(models.Model):
	title = models.CharField(max_length=100,verbose_name = "Title")
	file = models.FileField(upload_to='uploads/%Y %m %d/')

	def __str__(self):
		return f'{self.title}'
		
	class Meta:
		verbose_name_plural = "Question Papers"