from . import db
from django.shortcuts import render, redirect


def login(request):
    try:
        # 获取用户是否登录的信息
        msg = request.session.pop("msg")
    except:
        msg = ''
    if request.method == "GET":
        return render(request, 'login.html', {"msg": msg})
    param = request.POST.dict()
    sql = "select * from t_user where username = %(username)s and password = %(password)s"
    user = db.query_one(sql, args=param)
    if user is None:
        return render(request, 'login.html', {"msg": "您输入的用户名或密码错误"})
    if user["s_type"] == "普通用户":
        return render(request, 'login.html', {"msg": "您不是管理员身份，进不去啊"})
    request.session["LOGIN_LOCAL_FLAG"] = user
    return redirect(to='index')


def index(request):
    return render(request, "index.html")


def billList(request):
    sql1 = "select * from t_supplier"
    sup = db.query_list(sql1)
    sql = "select * from t_bill order by code"
    data = db.query_list(sql)
    return render(request, 'billList.html', {"data": data, "sup": sup})


def providerlist(request):
    sql = "select * from t_supplier t order by t.code"
    data = db.query_list(sql)
    return render(request, 'providerlist.html', {"data": data})


def change_pwd(request):
    user = db.get_current_user_id(request)
    id = user["id"]
    pwd = user["password"]
    if request.method == "GET":
        return render(request, 'change_pwd.html')
    param = request.POST.dict()
    oldpwd = param["oldPassword"]
    newpwd = param["newPassword"]
    if oldpwd != pwd:
        return render(request, 'change_pwd.html', {"msg": "密码不正确"})
    sql = "update t_user set password=%s where id=%s"
    db.update(sql, args=(newpwd, id))
    request.session.clear_expired()
    request.session.flush()
    return render(request, 'login.html', {"msg": "密码已修改,请重新登陆"})


def logout(request):
    request.session.clear_expired()
    request.session.flush()
    return redirect(to='/')
