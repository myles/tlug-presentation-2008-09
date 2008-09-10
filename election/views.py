# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404

from election.models import District, Candidate, Party

def index(request):
	districts = District.objects.all()
	parties = Party.objects.all()
	
	return render_to_response('election/index.html', { 'districts': districts, 'parties': parties })

def district_detail(request, district_slug):
	try:
		district = District.objects.get(slug=district_slug)
	except District.DoesNotExist:
		raise Http404
	
	return render_to_response('election/district_detail.html', { 'district': district })

def candidate_detail(request, district_slug, candidate_id):
	try:
		district = District.objects.get(slug=district_slug)
	except District.DoesNotExist:
		raise Http404
	
	try:
		candidate = Candidate.objects.get(pk=candidate_id)
	except Candidate.DoesNotExist:
		raise Http404
	
	return render_to_response('election/candidate_detail.html', { 'district': district, 'candidate': candidate })

def party_list(request):
	parties = Party.objects.all()
	
	return render_to_response('election/party_list.html', { 'parties': parties })

def party_detail(request, party_slug):
	try:
		party = Party.objects.get(slug=party_slug)
	except Party.DoesNotExist:
		raise Http404
	
	return render_to_response('election/party_detail.html', { 'party': party })