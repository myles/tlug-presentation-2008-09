from django.db import models
from django.db.models import permalink

# Create your models here.

class District(models.Model):
	title				= models.CharField('Title', max_length=200)
	slug				= models.SlugField('Slug', unique=True)
	current_incumbent	= models.CharField('Title', max_length=225)
	population			= models.IntegerField('Population', blank=True, null=True)
	electors			= models.IntegerField('Electors', blank=True, null=True)
	
	class Meta:
		verbose_name = 'district'
		verbose_name_plural = 'districts'
		db_table = 'election_districts'
	
	@permalink
	def get_absolute_url(self):
		return ('district_detail', None, {
			'district_slug':	self.slug,
		})
	
	def __unicode__(self):
		return u'%s' % self.title

class Party(models.Model):
	title			= models.CharField('Title', max_length=200)
	slug			= models.SlugField('Slug', unique=True)
	
	class Meta:
		verbose_name = 'party'
		verbose_name_plural = 'parties'
		db_table  = 'election_parties'
	
	@permalink
	def get_absolute_url(self):
		return ('party_detail', None, {
			'party_slug':	self.slug,
		})
	
	def __unicode__(self):
		return u'%s' % self.title

class Candidate(models.Model):
	first_name		= models.CharField('First name', max_length=100)
	last_name		= models.CharField('Last name', max_length=100)
	
	party			= models.ForeignKey(Party)
	district		= models.ForeignKey(District)
	
	class Meta:
		verbose_name = 'candidate'
		verbose_name_plural = 'candidates'
		db_table = 'election_candidates'
	
	@permalink
	def get_absolute_url(self):
		return ('candidate_detail', None, {
			'candidate_id':	self.pk,
			'district_slug':	self.district.slug,
		})
	
	@property
	def full_name(self):
		return u"%s %s" % (self.first_name, self.last_name)
	
	@property
	def is_current_incumbent(self):
		if self.full_name == self.district.current_incumbent:
			return True
		else:
			return False
	
	def __unicode__(self):
		return '%s' % self.full_name
