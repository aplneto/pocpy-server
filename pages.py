def require_authentication(func):
    def authenticate(*args, **kwargs):
        request = args[0]
        psw = request.get('psw', '')
        if psw == "123456":
            return func(*args, **kwargs)
        return "Authentication Error"
    return authenticate

@require_authentication
def render_page(request):
    usr = request['usr']
    return "Welcome, {usr}".format(usr=usr)