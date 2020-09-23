from django.db import models

class Sem1(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	ECAS130C_T = models.CharField(max_length=2,blank=True)
	SCDE130C_T = models.CharField(max_length=2,blank=True)
	EEDC132C_T = models.CharField(max_length=2,blank=True)
	IIPG132C_T = models.CharField(max_length=2,blank=True)
	SEGP132C_T = models.CharField(max_length=2,blank=True)
	IITC102C_L = models.CharField(max_length=2,blank=True)
	EEDC132C_L = models.CharField(max_length=2,blank=True)
	IIPG132C_L = models.CharField(max_length=2,blank=True)
	SEGP132C_L = models.CharField(max_length=2,blank=True)
	MPCN102C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 1"


class Sem2(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	SPAS230C_T = models.CharField(max_length=2,blank=True)
	IDMA230C_T = models.CharField(max_length=2,blank=True)
	EDES232C_T = models.CharField(max_length=2,blank=True)
	MPOM230C_T = models.CharField(max_length=2,blank=True)
	ICOA230C_T = models.CharField(max_length=2,blank=True)
	IDST232C_T = models.CharField(max_length=2,blank=True)
	EDES232C_L = models.CharField(max_length=2,blank=True)
	IDST232C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 2"

class Sem3(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	IOPS332C_T = models.CharField(max_length=2,blank=True)
	SMAT330C_T = models.CharField(max_length=2,blank=True)
	IOOM330C_T = models.CharField(max_length=2,blank=True)
	EMIP332C_T = models.CharField(max_length=2,blank=True)
	ITOC330C_T = models.CharField(max_length=2,blank=True)
	IOPS332C_L = models.CharField(max_length=2,blank=True)
	IOOM332C_L = models.CharField(max_length=2,blank=True)
	EMIP332C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 3"


class Sem4(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	IDAA432C_T = models.CharField(max_length=2,blank=True)
	SMAT430C_T = models.CharField(max_length=2,blank=True)
	EPCO432C_T = models.CharField(max_length=2,blank=True)
	IDBM432C_T = models.CharField(max_length=2,blank=True)
	IPPL430C_T = models.CharField(max_length=2,blank=True)
	IDAA432C_L = models.CharField(max_length=2,blank=True)
	EPCO432C_L = models.CharField(max_length=2,blank=True)
	IDBM432C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 4"

class Sem5(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	ECAS130C_T = models.CharField(max_length=2,blank=True)
	SCDE130C_T = models.CharField(max_length=2,blank=True)
	EEDC132C_T = models.CharField(max_length=2,blank=True)
	IIPG132C_T = models.CharField(max_length=2,blank=True)
	SEGP132C_T = models.CharField(max_length=2,blank=True)
	IITC102C_L = models.CharField(max_length=2,blank=True)
	EEDC132C_L = models.CharField(max_length=2,blank=True)
	IIPG132C_L = models.CharField(max_length=2,blank=True)
	SEGP132C_L = models.CharField(max_length=2,blank=True)
	MPCN102C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 5"

class Sem6(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	ECAS130C_T = models.CharField(max_length=2,blank=True)
	SCDE130C_T = models.CharField(max_length=2,blank=True)
	EEDC132C_T = models.CharField(max_length=2,blank=True)
	IIPG132C_T = models.CharField(max_length=2,blank=True)
	SEGP132C_T = models.CharField(max_length=2,blank=True)
	IITC102C_L = models.CharField(max_length=2,blank=True)
	EEDC132C_L = models.CharField(max_length=2,blank=True)
	IIPG132C_L = models.CharField(max_length=2,blank=True)
	SEGP132C_L = models.CharField(max_length=2,blank=True)
	MPCN102C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 6"

class Sem7(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	ECAS130C_T = models.CharField(max_length=2,blank=True)
	SCDE130C_T = models.CharField(max_length=2,blank=True)
	EEDC132C_T = models.CharField(max_length=2,blank=True)
	IIPG132C_T = models.CharField(max_length=2,blank=True)
	SEGP132C_T = models.CharField(max_length=2,blank=True)
	IITC102C_L = models.CharField(max_length=2,blank=True)
	EEDC132C_L = models.CharField(max_length=2,blank=True)
	IIPG132C_L = models.CharField(max_length=2,blank=True)
	SEGP132C_L = models.CharField(max_length=2,blank=True)
	MPCN102C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 7"

class Sem8(models.Model):
	enroll_no = models.CharField(max_length=10, primary_key=True,verbose_name = "Enrollment Number")
	ECAS130C_T = models.CharField(max_length=2,blank=True)
	SCDE130C_T = models.CharField(max_length=2,blank=True)
	EEDC132C_T = models.CharField(max_length=2,blank=True)
	IIPG132C_T = models.CharField(max_length=2,blank=True)
	SEGP132C_T = models.CharField(max_length=2,blank=True)
	IITC102C_L = models.CharField(max_length=2,blank=True)
	EEDC132C_L = models.CharField(max_length=2,blank=True)
	IIPG132C_L = models.CharField(max_length=2,blank=True)
	SEGP132C_L = models.CharField(max_length=2,blank=True)
	MPCN102C_L = models.CharField(max_length=2,blank=True)
	SGPI = models.DecimalField(max_digits=4, decimal_places=2)
	class Meta:
		verbose_name_plural = "Semester 8"