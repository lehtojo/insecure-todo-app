from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import List, ListItem

@login_required
def listView(request, list_id):
	list = List.objects.get(id=list_id)
	items = ListItem.objects.filter(list=list)
	return render(request, 'pages/list.html', {'name': list.name, 'items': items})


@login_required
@csrf_exempt
def createView(request):
	name = request.POST.get('name')
	list = List.objects.create(user=request.user, name=name)
	list.save()

	return redirect('/')


@login_required
def removeView(request):
	id = request.POST.get('id')
	list = List.objects.get(id=id)
	list.delete()

	return redirect('/')


@login_required
def addItemView(request, list_id):
	text = request.POST.get('text')
	list = List.objects.get(id=list_id)
	item = ListItem.objects.create(list=list, text=text)
	item.save()

	return redirect(f'/list/{list_id}')


@login_required
def removeItemView(request, list_id, item_id):
	item = ListItem.objects.get(id=item_id)
	item.delete()

	return redirect(f'/list/{list_id}')


@login_required
def homePageView(request):
	lists = List.objects.filter(user=request.user)
	return render(request, 'pages/index.html', {'lists': lists})
