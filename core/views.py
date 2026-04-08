from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
import uuid
from .models import Account
from students.models import Student

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        phone = data.get('phone')
        student_name = data.get('student_name')
        student_birth_date = data.get('student_birth_date')

        if not all([username, password, phone, student_name, student_birth_date]):
            return Response({"error": "缺少必填字段(username, password, phone, student_name, student_birth_date)"}, status=status.HTTP_400_BAD_REQUEST)

        if Account.objects.filter(username=username).exists():
            return Response({"error": "用户名已存在"}, status=status.HTTP_400_BAD_REQUEST)

        # 创建账号
        account = Account.objects.create(
            username=username,
            password=make_password(password),
            phone=phone
        )

        # 创建关联学员
        Student.objects.create(
            account_id=account.id,
            name=student_name,
            birth_date=student_birth_date,
            parent_name=username,
            phone=phone
        )

        return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return Response({"error": "请输入用户名和密码"}, status=status.HTTP_400_BAD_REQUEST)

        account = Account.objects.filter(username=username).first()
        if not account or not check_password(password, account.password):
            return Response({"error": "用户名或密码错误"}, status=status.HTTP_401_UNAUTHORIZED)

        # 生成 sessionId
        session_id = uuid.uuid4().hex
        
        # 缓存 sessionId，30天过期
        timeout = 30 * 24 * 3600
        cache.set(f"session:{session_id}", account.id, timeout=timeout)

        # 构造响应并设置 cookie
        response = Response({"message": "登录成功", "sessionId": session_id})
        response.set_cookie(
            'sessionId', 
            session_id, 
            max_age=timeout,
            httponly=True,
            samesite='Lax'
        )
        
        return response
