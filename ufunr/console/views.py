from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from console.models import User

def index(request):
    user_list = User.objects.all()
    context = { 'user_list': user_list }
    return render(request, 'console/index.html', context)

def validuser(request):
    user_list = User.objects.all()
    context = { 'user_list': user_list }
    return render(request, 'console/validuser.html', context)

def expireduser(request):
    user_list = User.objects.all()
    context = { 'user_list': user_list }
    return render(request, 'console/expireduser.html', context)

def updateuserinfo(request, account_id, valid_days, data_left, is_deleted):
    try:
      user = User.objects.get(account_id=account_id)
      user.valid_days=valid_days
      user.data_left=data_left
      user.is_deleted=is_deleted
    except User.DoesNotExist:
      user = User(account_id=account_id, valid_days=valid_days, data_left=data_left, is_deleted=is_deleted)

    user.save()
    user_list = User.objects.all()
    context = { 'user_list': user_list }
    return render(request, 'console/index.html', context)