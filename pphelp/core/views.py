# -*-coding:utf-8-*-
from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from core.models import Group_info, Suggestion, User
from django.contrib.auth import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = User.objects.create_user(username=username, password=password, email=email)
        status = {'register_info': user}
        return render_to_response('user.html', status)  # change user.html content
    else:
        return render(request, 'signin.html')


@csrf_exempt
def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        status = {'login_info': user}
        if user is not None:
            login(request, user)
            return user_center(request)
        else:
            status = {'info': 'username or password is wrong'}
            return render_to_response('login.html', status)
    else:
        return render(request, 'login.html')


@csrf_exempt
@login_required
def user_center(request):
    status = {'info': '', 'information': ''}  # the class has already yuyue
    user = request.user
    a = User.objects.get(username=user)
    info = a.group_info_set.all()
    information = a.myuser_set.all()
    return render_to_response('user.html', locals())


@csrf_exempt
@login_required
def change_info(request):
    if request.method == 'POST':
        gender = request.POST.get('gender', None)
        city = request.POST.get('city', None)
        school = request.POST.get('school', None)
        birthday = request.POST.get('birthday', None)
        email = request.POST.get('email', None)

        information = {'change_result': ''}

        user = request.user
        a = User.objects.get(username=user)
        data = a.user_info_set.all()
        if data.count() == 1:
            # change
            data.update(gender=gender, city=city, school=school, birthday=birthday, email=email)


        else:
            # create and connect
            info = User_info.objects.create(gender=gender, city=city, school=school, birthday=birthday, email=email)
            info.users.add(a)
        information['change_result'] = 'change success'
        return render_to_response('user.html', information)


@csrf_exempt
@login_required
def class_info(request):
    status = {'info': ''}
    data = Group_info.objects.all()
    status['info'] = data
    return render_to_response('class.html', status)


@csrf_exempt
@login_required
def appoint(request):
    status = {'info': ''}
    user = request.user
    items = Group_info.objects.all()
    for item in items:
        if item.teacher in request.POST:
            status = {'info': item,}
    a = User.objects.get(username=user)
    b = status['info']
    if a in b.groups_info.all():
        sta = {'appoint_info': '预约失败或者已经预约'}
    else:
        b.groups_info.add(a)
        b.save()
        sta = {'appoint_info': '预约成功'}
    return render_to_response('class.html',sta)


@csrf_exempt
@login_required
def teacher_list(request):
    status = {'info': ''}
    data = Group_info.objects.all()
    status['info'] = data
    return render_to_response('teacher.html', status)


@csrf_exempt
@login_required
def suggestion(request):
    if request.method == 'POST':
        sug = request.POST.get('suggestion', None)
        Suggestion.objects.create(suggestion=sug)
        status = {'info': '感谢您的反馈'}
        return render_to_response('suggestion', status)
    else:
        return render(request, 'suggestion.html')

# @csrf_exempt
# def checkSignature(request):
# 	signature=request.GET.get('signature',None)
# 	timestamp=request.GET.get('timestamp',None)
# 	nonce=request.GET.get('nonce',None)
# 	echostr=request.GET.get('echostr',None)
# 	#这里的token我放在setting，可以根据自己需求修改
# 	token=TOKEN
# 	tmplist=[token,timestamp,nonce]
# 	tmplist.sort()
# 	tmpstr="%s%s%s"%tuple(tmplist)
# 	tmpstr=hashlib.sha1(tmpstr.encode('utf8')).hexdigest()
# 	if tmpstr==signature:
# 		return echostr
# 	else:
# 		return error
# @csrf_exempt
# def weixin(request):
# 	if request.method=='GET':
# 		response=HttpResponse(checkSignature(request))
# 		return response
# 	else:
# 		return HttpResponse('Hello World')
# def authorization(request):
#     code = request.GET.get('code')
#     api = WeixinAPI(appid=APP_ID,
#                     app_secret=APP_SECRET,
#                     redirect_uri=REDIRECT_URI)
#     auth_info = api.exchange_code_for_access_token(code=code)
#     api = WeixinAPI(access_token=auth_info['access_token'])
#     resp = api.user(openid=auth_info['openid'])
#     return jsonify(resp)
# def weblogin(request):
#     return redirect('https://open.weixin.qq.com/connect/qrconnect?appid=wx478762de33427c1d&redirect_uri=http%3A%2F%2Fzhang.tunnel.qydev.com%2Foauth&response_type=code&scope=snsapi_login&state=STATE#wechat_redirect')
# wc = Wechat(APP_ID,APP_SECRET)
# def wlogin(request):
#     urlen = urllib.parse.quote("http://zhang.tunnel.qydev.com/oauth")
#     url = wc.get_connect_url(urlen)
#     return redirect(url)
# def oauth(request):
#     resp = wc.get_access_token(self, request.GET.get('code'))
#     access_token = resp.access_token
#     userinfo = wc.get_userinfo(access_token)
#     return HttpResponse("nickname:" + userinfo.nickname)
