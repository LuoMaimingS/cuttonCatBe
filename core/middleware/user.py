from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.http import JsonResponse
from core.models import Account

class UserAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        拦截请求，解析 Cookie 中的 sessionId 并挂载 Account 对象到 request 上
        """
        # 初始化为空
        request.account = None
        
        # 1. 从 cookie 获取 sessionId
        session_id = request.COOKIES.get('sessionId')
        
        # 2. 如果携带了 sessionId，去缓存里查
        if session_id:
            account_id = cache.get(f"session:{session_id}")
            if account_id:
                # 获取对应的用户对象
                request.account = Account.objects.filter(id=account_id).first()

        # 3. (可选) 全局拦截示例：如果不在白名单路径且未登录，则直接返回 401
        # 白名单：登录、注册、Admin后台等不需要校验
        # whitelist = ['/api/v1/auth/login/', '/api/v1/auth/register/', '/admin/']
        # is_whitelist = any(request.path.startswith(path) for path in whitelist)
        # 
        # if not is_whitelist and not request.account:
        #     return JsonResponse({"error": "未登录或登录已过期，请重新登录"}, status=401)

        return None
