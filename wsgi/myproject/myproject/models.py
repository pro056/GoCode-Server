from django.db import models 

class User(models.Model):
	user_id = models.CharField (max_length=50, primary_key=True)
	password = models.CharField (max_length=50)
	first_name = models.CharField (max_length=128)
	last_name = models.CharField (max_length=128)
	email_id = models.EmailField()
	chef_handle = models.CharField(max_length=50, default = '-')
	tc_handle = models.CharField(max_length=50, default = '-')
	forces_handle = models.CharField(max_length=50, default = '-')
	spoj_handle = models.CharField(max_length=50, default = '-')
	hackere_handle = models.CharField(max_length=50, default = '-')
	hackerr_handle = models.CharField(max_length=50, default = '-')
	kaggle_handle  = models.CharField(max_length=50, default = '-')

class Running_Contests(models.Model):
	contest_name = models.CharField (max_length = 128)
	contest_duration = models.CharField(max_length =10)
	contest_start_time = models.CharField(max_length =15)
	contest_end_time = models.CharField(max_length =15)
	contest_site = models.URLField()
	contest_status = models.PositiveSmallIntegerField(default=2)


class Future_Contests(models.Model):
	contest_name = models.CharField (max_length = 128)
	contest_duration = models.CharField(max_length =10)
	contest_start_time = models.CharField(max_length =15)
	contest_end_time = models.CharField(max_length =15)
	contest_site = models.URLField()
	contest_status = models.PositiveSmallIntegerField(default=3)


class Past_Contests(models.Model):
	contest_name = models.CharField (max_length = 128)
	contest_duration = models.CharField(max_length =10)
	contest_start_time = models.CharField(max_length =15)
	contest_end_time = models.CharField(max_length =15)
	contest_site = models.URLField()
	contest_status = models.PositiveSmallIntegerField(default=1)