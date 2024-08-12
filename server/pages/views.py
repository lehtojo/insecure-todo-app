from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import List, ListItem
import re

normal_text_pattern = r'^[a-zA-Z0-9\s.,!?-]*$'

@login_required
def listView(request, list_id):
	list = List.objects.get(id=list_id)

	# Verifies the requesting user owns the list (fix)
	# if list.user != request.user:
	# 	return HttpResponseBadRequest("Permission denied")

	items = ListItem.objects.filter(list=list)
	return render(request, 'pages/list.html', {'name': list.name, 'items': items})


@login_required
def createView(request):
	name = request.POST.get('name')

	# Verifies the list name doesn't contain illegal characters (fix)
	# if not re.match(normal_text_pattern, name):
	# 	return HttpResponseBadRequest("Illegal list name")

	list = List.objects.create(user=request.user, name=name)
	list.save()

	return redirect('/')


@login_required
def removeView(request):
	id = request.POST.get('id')
	list = List.objects.get(id=id)

	# Verifies the requesting user owns the list (fix)
	# if list.user != request.user:
	# 	return HttpResponseBadRequest("Permission denied")

	list.delete()

	return redirect('/')


# Remove "@csrf_exempt" to protect against CSRF (fix)
@login_required
@csrf_exempt
def addItemView(request, list_id):
	text = request.POST.get('text')

	# Verifies the task item text doesn't contain illegal characters (fix)
	# if not re.match(normal_text_pattern, text):
	# 	return HttpResponseBadRequest("Illegal item text")

	list = List.objects.get(id=list_id)

	# Verifies the requesting user owns the list (fix)
	# if list.user != request.user:
	# 	return HttpResponseBadRequest("Permission denied")

	item = ListItem.objects.create(list=list, text=text)
	item.save()

	return redirect(f'/list/{list_id}')


# Remove "@csrf_exempt" to protect against CSRF (fix)
@login_required
@csrf_exempt
def removeItemView(request, list_id, item_id):
	item = ListItem.objects.get(id=item_id)

	# Verifies the requesting user owns the list (fix)
	# if item.list.user != request.user:
	# 	return HttpResponseBadRequest("Permission denied")

	item.delete()

	return redirect(f'/list/{list_id}')


@login_required
def homePageView(request):
	lists = List.objects.filter(user=request.user)
	return render(request, 'pages/index.html', {'lists': lists})
