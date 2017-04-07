from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models
from datetime import datetime

# Create your models here.

class Merchants(models.Model):
	user = models.OneToOneField(User)
	mobile_number=models.CharField(max_length=300, blank=False)
	address=models.CharField(max_length=300, blank=False)
	business_name=models.CharField(max_length=300, blank=True)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['-date']
		verbose_name='Merchant'
		verbose_name_plural='Merchants'
	def __unicode__(self):
		return self.mobile_number



class Contacts(models.Model):
	first_name=models.CharField(max_length=300)
	last_name=models.CharField(max_length=300)
	email=models.CharField(max_length=300)
	mobile_number=models.CharField(max_length=300)
	description=models.TextField(blank=False)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['date']
		verbose_name="contact message"
		verbose_name_plural="contact messages"
	def __unicode__(self):
		return  self.mobile_number
class BlogCategories(models.Model):
	title=models.CharField(max_length=300)
	description=models.TextField(blank=False)
	slug=models.SlugField(blank=False)
	is_active=models.BooleanField(default=False)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['date']
		verbose_name = "Blog Category"
		verbose_name_plural="Blog Categories"
	def __unicode__(self):
		return self.title
class BlogPost(models.Model):
	LIVE_STATUS=1
	DRAFT_STATUS=2
	HIDDEN_STATUS=3
	STATUS_CHOICES=((LIVE_STATUS, 'live'), (DRAFT_STATUS, 'draft'), (HIDDEN_STATUS, 'hidden'))
	title=models.CharField(max_length=300)
	body=models.TextField(blank=False)
	category=models.ForeignKey(BlogCategories)
	featured = models.BooleanField(default=True)
	status=models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	slug=models.SlugField()
	author=models.ForeignKey(User)
	pub_date=models.DateTimeField(default=datetime.now)
	image1=models.ImageField(upload_to="images", verbose_name='Images', blank=False)
	image2=models.ImageField(upload_to="images", verbose_name='Images', blank=True)
	image3=models.ImageField(upload_to="images", verbose_name='Images', blank=True)
	class Meta:
		ordering=['pub_date']
		verbose_name='Blog Post'
		verbose_name_plural="blog posts"
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return self.slug
class Tags(models.Model):
	title=models.CharField(max_length=300)
	decription=models.TextField(blank=False)
	is_active=models.BooleanField(default=True)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['date']
		verbose_name='Tag'
		verbose_name_plural="Tags"

class documentation(models.Model):
	topic=models.CharField(max_length=200)
	tag=models.ForeignKey(Tags)
	description=models.TextField(blank=False)
	slug=models.SlugField()
	author=models.ForeignKey(User)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['date']
		verbose_name="Documentation"
		verbose_name_plural="Documentations"
	def __unicode__(self):
		return  self.topic
	def get_absolute_url(self):
		return self.slug

class Team(models.Model):
	frist_name=models.CharField(max_length=300, unique=False)
	last_name=models.CharField(max_length=300, unique=False)
	title=models.CharField(max_length=300, unique=True)
	contact_email=models.EmailField(max_length=300, unique=False)
	profile_picture=models.ImageField(upload_to="avatars/", verbose_name='Images', blank=False)
	is_active=models.BooleanField(default=True)
	class Meta:
		ordering=['frist_name']
		verbose_name='Team Member'
		verbose_name_plural='Team Members'
	def __unicode__(self):
		return self.frist_name
class JobCategories(models.Model):
	title=models.CharField(max_length=300)
	description=models.TextField(blank=True)
	is_active=models.BooleanField(default=True)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['date']
		verbose_name='Job Category'
		verbose_name_plural='Job Categories'
	def __unicode__(self):
		return self.title


class JobPosting(models.Model):
	job_category=models.ForeignKey(JobCategories)
	job_title=models.CharField(max_length=300,unique=True)
	job_description=models.TextField(blank=False)
	job_location=models.CharField(max_length=300)
	vacancies_available=models.CharField(max_length=300)
	posted_on=models.DateTimeField(default=datetime.now)
	class Meta:
		ordering=['-posted_on']
		verbose_name='Job Posting'
		verbose_name_plural='Job postings'
	def __unicode__(self):
		return self.job_title








