# Create your views here.
#coding:utf-8
#import builtins
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext

from django.views.decorators.csrf import csrf_exempt

import random
from .models import Student
# Create your views here.
from django.core.context_processors import csrf

def hello(request):
	return HttpResponse("我是django的第一个例子！")


def myhtml(request):
	return render(request,'a.html',locals())


def bb(request):
	return render(request,'bb.html')
#访问首页
def beginAdd(request):
	return render(request,'add.html')
#保存数据
@csrf_exempt
def add(request):
   # c={}
   id=request.POST['id']
   name=request.POST['name']
   age=request.POST['age']
   st=Student()
   if  len(id)  > 0 :
	   print("id不是null")
	   st.id=id;
   st.age=age
   st.name=name
   st.save()
   return HttpResponseRedirect("/q")

#查询所�?
def query(request):
	b=Student.objects.all()

	#for  e in b:
		#print(e.id,"   ",e.age,"   ",e.name)

	return render(request,'curd.html',{'data':b})
#显示一条数�?
def showUid(request):
	id=request.GET['id'];
	bb=Student.objects.get(id=id)
	return render(request,'update.html',{'data':bb})
#删除数据
def delByID(request):
	id=request.GET['id'];
	bb=Student.objects.get(id=id)
	bb.delete()
	return HttpResponseRedirect("/q")



def show(request):


		return render(request,'data.html',{'datas':datas})
