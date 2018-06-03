from django.db import models

# Create your models here.
class Member(models.Model):
	pass

class Authorization(models.Model):
	authorizationid=models.CharField(max_length=11,blank=False)
	memberid=models.CharField(max_length=11,blank=False)
	ndc_no=models.CharField(max_length=11,blank=False)
	startdate=models.DateField()
	enddate=models.DateField()
	createdate=models.DateTimeField(auto_now_add=True)
	updatedate=models.DateTimeField(auto_now=True )