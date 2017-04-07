from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from app.models import *



# Create your views here.


def home(request):
	return render_to_response("index.html",{})
@csrf_exempt
def register_merchant(request):
	context=RequestContext(request)
	if request.method=="POST":
		data={}
		from processes import get_merchant_data, save_merchant, save_merchant_profile, send_email
		get_merchant_data.run(request.POST,data)
		save_merchant.run(data)
		save_merchant_profile.run(data)
		send_email.run(data)
		messages.add_message(request, messages.INFO, 'Hello world.')
	return render_to_response('register-merchant.html',{},context)

def wallet(request):
	return  render_to_response("wallet.html",{})
def overview(request):
	return  render_to_response("overview.html",{})
def documentation(request):
	return  render_to_response('documentation.html',{})

def about(request):
	return render_to_response("about.html",{})
def team(request):
	members=Team.objects.filter(is_active=True)
	engineer_jobs=JobPosting.objects.filter(job_category=1)
	operations_jobs=JobPosting.objects.filter(job_category=2)
	print operations_jobs
	return  render_to_response("team.html",{'members':members,
		'engineer_jobs':engineer_jobs,
		'operations_jobs':operations_jobs})
@csrf_exempt
def contact(request):
	context=RequestContext(request)
	if request.method=="POST":
		data={}
		from processes import  get_contact_details,save_contact_data,email_new_contact
		get_contact_details.run(request.POST, data)
		save_contact_data.run(data)
		email_new_contact.run(data)
	return render_to_response("contact.html",{})
def legal(request):
	return  render_to_response('legal.html',{})
def blog_category(request, slug):
	return render_to_response('blog_category.html',{
	'object':get_object_or_404(BlogCategories, slug=slug)},RequestContext(request))

def blog(request):
	blogposts=BlogPost.objects.filter(featured=True)
	blog_categories=BlogCategories.objects.all()
	return render_to_response("blog.html",{"blog_categories":blog_categories,"blogposts":blogposts,})