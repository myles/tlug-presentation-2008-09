from django.conf.urls.defaults import *

urlpatterns = patterns('election.views',
	url(r'^parties/(?P<party_slug>[-\w]+)/$',
		view	= 'party_detail',
		name	= 'party_detail'
	),
	url(r'^parties/$',
		view	= 'party_list',
		name	= 'party_list'
	),
	url(r'^(?P<district_slug>[-\w]+)/(?P<candidate_id>\d+)/$',
		view	= 'candidate_detail',
		name	= 'candidate_detail'
	),
	url(r'^(?P<district_slug>[-\w]+)/$',
		view	= 'district_detail',
		name	= 'district_detail'
	),
	url(r'^$',
		view	= 'index',
		name	= 'election_index',
	),
)