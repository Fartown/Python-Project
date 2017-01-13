from django.shortcuts import render
from labmanage.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.db.models import F

# Create your views here.
def home(request):
    try:
        fieldlist = Field.objects.all()
        news_list = News.objects.all()[:5]
        engin_list = Engineer.objects.all()[:10]
        paper_list = Paper.objects.all()[:5]
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
        news = News.objects.all()
        banner = Banner.objects.all()
        device = Device.objects.all()[:4]
    except News.DoesNotExist:
        raise Http404
    return render(request,'enhtml/index.html',locals())
def device(request):
    fieldlist = Field.objects.all()
    fieldtag = []
    for field in fieldlist:
        i=0
        fieldtag.insert(i,field.tag)
    fieldtag = list(set(fieldtag))
    banner = Banner.objects.all()
    device = Device.objects.all()
    return render(request,'enhtml/device.html',locals())
def news(request):
    try:
        news_list = News.objects.all()
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
        paginator = Paginator(news_list, 10)
        page = request.GET.get('page')
        try :
            news_list = paginator.page(page)
        except PageNotAnInteger :
            news_list = paginator.page(1)
        except EmptyPage :
            news_list = paginator.paginator(paginator.num_pages)
    except News.DoesNotExist:
        raise Http404
    return render(request,'enhtml/news.html',locals())
def detail(request,id):
    try:
        post = News.objects.get(id=str(id))
    except News.DoseNotExist:
        raise Http404
    return render(request,'enhtml/news1.html',{'post':post})
def technology(request):
    try:
        engin_list = Engineer.objects.all()
        paginator = Paginator(engin_list, 10)
        page = request.GET.get('page')
        try :
            engin_list = paginator.page(page)
        except PageNotAnInteger :
            engin_list = paginator.page(1)
        except EmptyPage :
            engin_list = paginator.paginator(paginator.num_pages)
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
    except Engineer.DoesNotExist:
        raise Http404
    return render(request,'enhtml/engineer.html',locals())
def engindetail(request,id):
    try:
        post = Engineer.objects.get(id=str(id))
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
    except Engineer.DoseNotExist:
        raise Http404
    return render(request,'enhtml/engineer1.html',{'post':post})
def person(request):
    fieldlist = Field.objects.all()
    fieldtag = []
    for field in fieldlist:
        i=0
        fieldtag.insert(i,field.tag)
    fieldtag = list(set(fieldtag))
    return render(request,'enhtml/teacher.html',locals())
def student(request):
    try:
        student_list = Student.objects.all()
        postdoctor = Student.objects.filter(education='博士后')
        doctor = Student.objects.filter(education='博士')
        master = Student.objects.filter(education='硕士')
        bachelor = Student.objects.filter(education='本科')
        graduate = Student.objects.filter(education='毕业生')
    except Student.DoesNotExist:
        raise Http404
    return render(request,'enhtml/student.html',locals())
def field(request):
    try:
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
            # print(fieldtag[i])
        fieldtag = list(set(fieldtag))
        fieldarticle = []
        for tag in fieldtag:
            fieldarticle.append(Field.objects.filter(tag=tag))
    except Field.DoesNotExist:
        raise Http404
    return render(request,'enhtml/field1.html',locals())
def fielddetail(request,id):
    try:
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
            # print(fieldtag[i])
        fieldtag = list(set(fieldtag))
        fieldarticle = []
        for tag in fieldtag:
            fieldarticle.append(Field.objects.filter(tag=tag))
    except Field.DoesNotExist:
        raise Http404
    try:
        post = Field.objects.get(id=str(id))
    except News.DoseNotExist:
        raise Http404
    return render(request,'enhtml/field1.html',locals())
def achieve(request):
    try:
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
        funds_list = Funds.objects.all()
        # 分页
        paginator = Paginator(funds_list, 20)
        page = request.GET.get('page')
        try :
            funds_list = paginator.page(page)
        except PageNotAnInteger :
            funds_list = paginator.page(1)
        except EmptyPage :
            funds_list = paginator.paginator(paginator.num_pages)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'enhtml/achieve1.html',locals())
def paper(request):
    try:
        paper_list = Paper.objects.all()
        paginator = Paginator(paper_list, 15)
        page = request.GET.get('page')
        try :
            paper_list = paginator.page(page)
        except PageNotAnInteger :
            paper_list = paginator.page(1)
        except EmptyPage :
            paper_list = paginator.paginator(paginator.num_pages)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'enhtml/achieve2.html',{'paper_list':paper_list})
def patent(request):
    try:
        patent_list = Patent.objects.all()
        paginator = Paginator(patent_list, 13)
        page = request.GET.get('page')
        try :
            patent_list = paginator.page(page)
        except PageNotAnInteger :
            patent_list = paginator.page(1)
        except EmptyPage :
            patent_list = paginator.paginator(paginator.num_pages)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'enhtml/achieve3.html',{'patent_list':patent_list})
def about(request):
    content = About.objects.all()[0].content
    return render(request,'enhtml/about.html',{'content':content})