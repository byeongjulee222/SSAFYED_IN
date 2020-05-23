from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password, make_password
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, UserNameSerializer, UserCreationSerializer, UserLoginSerializer, UserUpdateSerializer, UserUpdatePasswordSerializer, MessageSerializer, MessageSendSerializer
from .models import User, Message
from portfolios.models import Tech
from rest_framework import generics
from django.core.mail import EmailMessage
import string
import random
from django.db.models import Q
from django_drf_filepond.models import TemporaryUpload
from django_drf_filepond.api import store_upload
import os

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
@permission_classes((AllowAny, ))
# @permission_classes((IsAuthenticated, ))
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    # if request.user != user:
    #     return HttpResponseForbidden()
        # return Response(status=403) 으로 작성해도 위와 같은 동작
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
# @login_required
@permission_classes((AllowAny, ))
def user_update(request, id):
    user = get_object_or_404(User, pk=id)
    # tech = Tech.objects.all()
    if request.method == 'POST':
        demo = request.data
        if request.data.get('profile_img'):
            filepond = get_object_or_404(TemporaryUpload, upload_id=request.data.get('profile_img'))
            if not os.path.exists(f'./media/{user}'):
                os.makedirs(f'./media/{user}')
            su = store_upload(filepond.upload_id, destination_file_path=f'{user}/{str(filepond.file_id)+filepond.upload_name}')
            filepond.delete()
        # url = 'http://i02b102.p.ssafy.io:8054/media/'+str(filepond.file)
            url = 'http://i02b102.p.ssafy.io:8054/media/'+str(su.file_path)
            demo['profile_img'] = url
        serializer = UserUpdateSerializer(data=demo, instance=user)
        # print('serializer', serializer)
        if serializer.is_valid(raise_exception=True):
            # print('request.data: ', request.data)
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'deleted!'})

    
@api_view(['POST'])
@permission_classes((AllowAny, ))
# @permission_classes((IsAuthenticated, ))
# @login_required
def password_update(request, id):
    user = get_object_or_404(User, pk=id)
    # print('request.data: ', request.data)
    user.password = request.data.get('password')
    # print('user: ', user)
    serializer = UserUpdatePasswordSerializer(data=request.data, instance=user)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # print('user: ', user)
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': '비밀번호 변경이 성공적으로 완료되었습니다.'})


@api_view(['GET'])
@permission_classes((AllowAny, ))
def user_name(request):
    user = User.objects.all()
    serializer = UserNameSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# 이 경우 회원가입 하는 경우에만 로그인여부를 판단하지 않도록 @permission_classes 데코레이터를 사용하고
# AllowAny를 튜플형태로 추가해준다.
@permission_classes((AllowAny, ))
def user_signup(request):
    # print('request: ', request.data)
    demo = request.data
    filepond = get_object_or_404(TemporaryUpload, upload_id=request.data.get('verified_img'))
    #username
    if not os.path.exists(f'./media/{filepond.upload_id}'):
        os.makedirs(f'./media/{filepond.upload_id}')
    su = store_upload(filepond.upload_id, destination_file_path=f'{filepond.upload_id}/{filepond.upload_name}')
    filepond.delete()
    # url = 'http://i02b102.p.ssafy.io:8054/media/'+str(su.file_path)
    url = 'http://i02b102.p.ssafy.io:8054/media/'+str(su.file_path)
    demo['verified_img'] = url
    serializer = UserCreationSerializer(data=demo)
    # filepond.delete()
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
    # else:
    #     print('NO!!!')


@api_view(['POST'])
@permission_classes((AllowAny, ))
def login(request):
    # print('####login####')
    serializer = UserLoginSerializer(data=request.data)
    # print('---login---')
    # print('serializer: ', serializer)
    # print(request.POST)
    if serializer.is_valid(raise_exception=True):
        # print('*****login*****111')
        # print(serializer.data)
        serializer.save()
        # auth_login(request.data, user)
        # print('*****auth_login')
        return Response({'message': '로그인이 성공적으로 완료되었습니다.'})


@login_required
def logout(request):
    auth_logout(request)
    return Response({'message': '로그아웃 되었습니다. '})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def password_send_mail(request):
    Len = 12
    string_pool = string.ascii_letters + string.digits
    result = ''
    for _ in range(Len):
        result += random.choice(string_pool)

    # print('request: ', request)
    # print('request.data: ', request.data)
    user = get_object_or_404(User, username=request.data.get('username'))
    
    # print('user: ', user)
    # print(user.nickname)
    # print(request.data.get('nickname'))
    if user.nickname == request.data.get('nickname'):
        user.password = result
        user.set_password(user.password)
        user.save()
        # print(user.password)
        # print('user: ', user)
        template = f'''
        비밀번호 재생성을 위해 임시 비밀번호를 발급해드렸습니다.
        비밀번호 : '{result}' 를 입력해주세요.
        '''
        # message = render_to_string()
        mail = EmailMessage(
            'SSAFYedIn 임시비밀번호 발급',                # 제목
            template,
            to=[f'{user}'],
            # 'username': user,
        )
        mail.send()
        
        return Response({'message': '메일을 성공적으로 보냈습니다.'})
    else:
        return Response(EOFError)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_authenticate(request):
    # user = get_object_or_404(User, pk=id)
    # print('request.data: ', request.data)
    # print('sendAuth: ', request.data.get('sendAuth_ssafy'))
    # serializer = UserUpdateSerializer(data=request.data)
    # print('key: ', request.data.keys())
    # for _ in range(2):
    # print(request.data)
    if 'sendAuth_ssafy' in request.data.keys():
        for u in request.data.get('sendAuth_ssafy'):
            # print('ssafy u: ', u)
            user = get_object_or_404(User, pk=u.get('id'))
            user.auth = u['auth']
            user.save()
    if 'sendAuth_recruit' in request.data.keys():
        # print('send recruit', request.data.keys())
        for u in request.data.get('sendAuth_recruit'):
            # print('u: ', u)
            user = get_object_or_404(User, pk=u.get('id'))
            user.auth = u['auth']
            user.save()

    return Response(request.data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def list_message(request, id):
    #여기서의 id는 로그인한 사람의 정보이다.
    messages_re = Message.objects.filter(Q(recipient_id=id)).order_by('-pk')
    messages_se = Message.objects.filter(Q(sender_id=id)).order_by('-pk')
    messages_read = Message.objects.filter(recipient_id=id,isRead=False).count()
    ### 내가 보낸 목록, 받은 목록 따로 보내줄지 프론트에 물어봀것 
    # 따로 필요하면 따로 만들어줄것. serializer1, serializer2 ...
    serializer_re = MessageSerializer(messages_re, many=True)
    serializer_se = MessageSerializer(messages_se, many=True)

    # 이미 읽은 값이라면 흐린글씨? 또는 표현을 다르게 해달라고 하기. 추가적으로 
    # 안 읽은 갯수가 필요하면 보내주자
    return Response([serializer_re.data, serializer_se.data, {'notread': messages_read}])


@api_view(['GET'])
# @login_required
# @permission_classes((AllowAny, ))
def read_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    # if request.user.id == message.recipient_id:
    if not message.isRead:
        message.isRead = True
        message.save()
        serializer = MessageSerializer(message)
        # print(serializer.data)
        return Response(serializer.data)
    return Response({'실패':'ㅜㅜ'})


@api_view(['POST'])
# @login_required
# id : 받는 쪽 (<int:pk>)
def send_message(request, re_id):
    to_user = get_object_or_404(User, pk=re_id)
    # 여기 .dict() 없애야할수도 있음 
    demo = request.data
    demo['recipient'] = to_user.pk
    # demo['sender'] = request.user.pk
    # print(demo)
    serializer = MessageSendSerializer(data=demo)
    # print('serializer: ', serializer)
    if serializer.is_valid():
        serializer.save()
        # return Response({'message': '메세지를 전송하였습니다.'})
        # print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({'실패':serializer.data})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_page(request):
    users = User.objects.order_by('-pk')
    text = request.data.get('search_text', '')
    if text != '':
        users = users.filter(nickname__icontains=text)
    serializer = UserSerializer(users, many=True, context={'request': request})

    return Response(serializer.data)



@api_view(['POST'])
@permission_classes((AllowAny, ))
def tech_page(request):
    users = User.objects.order_by('-pk')
    text = request.data.get('search_text', '')
    # print(users)
    if text[0] == '#':
        tech = Tech.objects.filter(tech_stack=text[1:])
        # print(tech.get('id'))
        for user in users:
            print(user)
            # print(user.tech_category)
        # print(users.get('tech_category'))
        # users = users.get('tech_category').filter(tech_category=tech)
    # for user in users:
    #     print('tech_category: ', user.get('tech_category'))
    if text != '':
        users = users.filter(nickname__icontains=text)
    serializer = UserSerializer(users, many=True, context={'request': request})

    return Response(serializer.data)
