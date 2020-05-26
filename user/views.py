from django.http import JsonResponse
from django.shortcuts import render, redirect
from myshopping import db


def index(request):
    sql = "select t.id,t.code,t.username,t.sex,t.birth,t.tel,t.s_type from t_user t order by t.code"
    user = db.query_list(sql)
    return render(request, 'userIndex.html', {"user": user})


def add(request):
    if request.method == 'GET':
        return render(request, 'userAdd.html')
    param = request.POST.dict()
    param.pop("userRemi")
    sql = """
        insert into t_user(code,username,password,sex,birth,tel,addr,s_type)values (
        %(code)s,%(username)s,%(password)s,%(sex)s,%(birth)s,%(tel)s,%(addr)s,%(s_type)s)
    """
    db.update(sql, args=param)
    return redirect(to='/user/index')


def detail(request, id):
    sql = "select * from t_user where id = %s"
    user = db.query_one(sql, args=(id,))
    return render(request, 'userDetail.html', {"user": user})


def check_code(request, code):
    sql = "select * from t_user where code = %s"
    user = db.query_one(sql, args=(code,))
    if user is None:
        return JsonResponse({"status": True, "msg": ""})
    return JsonResponse({"status": False, "msg": "该编码已存在"})


def check_tel(request, tel):
    sql = "select * from t_user where tel=%s"
    user = db.query_one(sql, args=(tel,))
    if user is None:
        return JsonResponse({"status": True, "msg": ""})
    return JsonResponse({"status": False, "msg": "手机号已被注册"})


def delete(request, id):
    sql = "delete from t_user where id = %s"
    db.update(sql, args=(id,))
    return JsonResponse({"isdel": True})


def update(request, id):
    if request.method == 'GET':
        sql = "select * from t_user where id = %s"
        user = db.query_one(sql, args=(id,))
        return render(request, 'userUpdate.html', {"user": user})
    param = request.POST.dict()
    param.setdefault("id", id)
    sql = """
        update t_user set username=%(username)s,sex=%(sex)s,birth=%(birth)s,
        tel=%(tel)s,addr=%(addr)s,s_type=%(s_type)s where id = %(id)s
    """
    db.update(sql, args=param)
    return redirect(to='/user/index')


def search(request):
    sear = request.POST.dict()["sear"]
    sql = "select * from t_user where username like %s order by code"
    user = db.query_list(sql, args=(f"%{sear}%",))
    return render(request, 'userIndex.html', {"user": user})
    # return redirect(to='/user/index', **{"user": user})
