from django.http import JsonResponse
from django.shortcuts import render, redirect
from myshopping import db


# Create your views here.
def provideradd(request):
    if request.method == "GET":
        return render(request, "provideradd.html")
    else:

        param = request.POST.dict()

        sql = "insert into t_supplier (code,s_name,contacts,tel,addr,fax,s_desc) values (%(code)s,%(s_name)s,%(contacts)s,%(tel)s,%(addr)s,%(fax)s,%(s_desc)s)"

        db.update(sql, args=param)

        return redirect(to="/providerlist")


def check_tel(request, tel):
    sql = "select * from t_supplier where tel=%s"
    user = db.query_one(sql, args=(tel,))

    if user is None:
        return JsonResponse({"status": True, "msg": ""})
    return JsonResponse({"status": False, "msg": "手机号已存在！！"})


def providerupdate(request, pk):
    if request.method == "GET":
        sql = "select * from t_supplier where id=%s"
        data = db.query_one(sql, args=(pk,))
        return render(request, "providerupdate.html", {"data": data})
    param = request.POST.dict()
    param.setdefault("id", pk)
    sql = "update t_supplier set code=%(code)s,s_name=%(s_name)s,contacts=%(contacts)s,tel=%(tel)s,addr=%(addr)s,fax=%(fax)s,create_time=now(),s_desc=%(s_desc)s where id = %(id)s"
    db.update(sql, args=param)
    return redirect(to="/providerlist")


def providerview(request, pk):
    sql = "select * from t_supplier where id=%s"

    data = db.query_one(sql, args=(pk,))

    return render(request, "providerview.html", {"data": data})


def search(request):
    search = request.POST.dict()["search"]
    sql = "select * from t_supplier where s_name like %s order by code"
    data = db.query_list(sql, args=(f"%{search}%",))
    return render(request, "providerlist.html", {"data": data})


def delete(request, id):
    # sql="delete from t_supplier where id = %s"
    sql = """
        delete a,b
        from t_supplier as a
        left join t_bill as b
        on a.s_name=b.sup_name
        where a.id=%s
    """
    db.update(sql, args=(id,))
    return JsonResponse({"isdel": True})
