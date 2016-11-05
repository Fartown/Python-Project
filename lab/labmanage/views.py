from django.shortcuts import render
from labmanage.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.db.models import F

# Create your views here.
def home(request):
    try:
        fieldlist = Field.objects.all()
        fieldtag = []
        for field in fieldlist:
            i=0
            fieldtag.insert(i,field.tag)
        fieldtag = list(set(fieldtag))
        news = News.objects.all()
        banner = Banner.objects.all()
    except News.DoesNotExist:
        raise Http404
    return render(request,'html/index.html',locals())
def news(request):
    try:
        news_list = News.objects.all()
        paginator = Paginator(news_list,2)
        page = request.GET.get('page')
        try :
            post_list = paginator.page(page)
        except PageNotAnInteger :
            post_list = paginator.page(1)
        except EmptyPage :
            post_list = paginator.paginator(paginator.num_pages)
    except News.DoesNotExist:
        raise Http404
    return render(request,'html/news.html',locals())
def detail(request,id):
    try:
        post = News.objects.get(id=str(id))
    except News.DoseNotExist:
        raise Http404
    return render(request,'html/news1.html',{'post':post})
def technology(request):
    try:
        engin_list = Engineer.objects.all()
    except Engineer.DoesNotExist:
        raise Http404
    return render(request,'html/engineer.html',{'engin_list':engin_list})
def engindetail(request,id):
    try:
        post = Engineer.objects.get(id=str(id))
    except Engineer.DoseNotExist:
        raise Http404
    return render(request,'html/engineer1.html',{'post':post})
def person(request):
    return render(request,'html/teacher.html')
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
    return render(request,'html/student.html',locals())
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
    return render(request,'html/field1.html',locals())
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
    return render(request,'html/field1.html',locals())
def achieve(request):
    try:
        funds_list = Funds.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'html/achieve1.html',{'funds_list':funds_list})
def paper(request):
    try:
        paper_list = Paper.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'html/achieve2.html',{'paper_list':paper_list})
def patent(request):
    try:
        patent_list = Patent.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'html/achieve3.html',{'patent_list':patent_list})
def about(request):
    content = About.objects.all()[0].content
    return render(request,'html/about.html',{'content':content})
class ArticleListView(ListView):
    template_name = 'html/news3.html'
    def get_queryset(self, **kwargs):
        object_list = News.objects.all().order_by(F('add_date').desc())[:300]
        paginator = Paginator(object_list, 4)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            object_list = paginator.page(paginator.num_pages)
        return object_list

