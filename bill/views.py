from django.shortcuts import render, redirect
from myshopping import db
from django.http import JsonResponse


# Create your views here.


def billAdd(request):
    if request.method == "GET":
        sql = "select * from t_supplier"
        sup = db.query_list(sql)
        return render(request, 'billAdd.html', {"sup": sup})
    param = request.POST.dict()
    sql = """
           insert into t_bill(code,s_name,unit,num,price,sup_name,state)
           values(%(code)s,%(s_name)s,%(unit)s,%(num)s,%(price)s,%(sup_name)s,%(state)s)
       """
    db.update(sql, args=param)
    return redirect(to="/billList")


def check_code(request, code):
    sql = "select * from t_bill where  code =%s"
    cod = db.query_one(sql, args=(code,))
    if cod is None:
        return JsonResponse({"status": True, "msg": ""})
    return JsonResponse({"status": False, "msg": "账单编码已存在"})


def billUpdate(request, pk):
    if request.method == "GET":
        sql = "select * from t_bill where  id=%s"
        data = db.query_one(sql, args=(pk,))
        sql = "select * from t_supplier"
        sup = db.query_list(sql)
        return render(request, 'billUpdate.html', {"data": data, "sup": sup})
    param = request.POST.dict()
    param.setdefault("id", pk)
    sql = """
          update t_bill set code = %(code)s, s_name = %(s_name)s ,unit = %(unit)s ,num = %(num)s, price = %(price)s,
          sup_name = %(sup_name)s ,state = %(state)s where id = %(id)s
       """
    db.update(sql, args=param)
    return redirect(to="/billList")


def billView(request, pk):
    sql = "select * from t_bill where  id=%s"
    data = db.query_one(sql, args=(pk,))
    return render(request, 'billView.html', {"data": data})


def dele(request, id):
    sql = "delete from t_bill where id=%s"
    db.update(sql, args=(id,))
    return JsonResponse({"isdel": True})


def query(request):
    sql = "select * from t_supplier"
    sup = db.query_list(sql)
    s_name = request.POST.dict()["s_name"]
    sup_name = request.POST.dict()["sup_name"]
    state = request.POST.dict()["state"]
    # sql = "select * from t_bill where s_name like %s and sup_name = %s  and state = %s order  by code"
    if s_name != '' and sup_name != '' and state != '':
        sql = "select * from t_bill where s_name  like %s and  sup_name=%s and state=%s order  by  code"
        data = db.query_list(sql, args=(f"%{s_name}%", sup_name, state))
    elif s_name != '' and sup_name != '' and state == '':
        sql = "select * from t_bill where s_name like %s and sup_name=%s  order  by  code"
        data = db.query_list(sql, args=(f"%{s_name}%", sup_name))
    elif s_name != '' and sup_name == '' and state != '':
        sql = "select * from t_bill where s_name  like %s and state=%s order  by  code"
        data = db.query_list(sql, args=(f"%{s_name}%", state))
    elif s_name == '' and sup_name != '' and state != '':
        sql = "select * from t_bill where  sup_name = %s and state=%s order  by  code"
        data = db.query_list(sql, args=(sup_name, state))
    elif s_name != '' and sup_name == '' and state == '':
        sql = "select * from t_bill where s_name like %s order  by  code"
        data = db.query_list(sql, args=(f"%{s_name}%",))
    elif s_name == '' and sup_name != '' and state == '':
        sql = "select * from t_bill where  sup_name = %s order  by  code"
        data = db.query_list(sql, args=(sup_name,))
    elif s_name == '' and sup_name == '' and state != '':
        sql = "select * from t_bill where state = %s order  by  code"
        data = db.query_list(sql, args=(state,))
    else:
        sql = "select * from t_bill where s_name like %s order  by  code"
        data = db.query_list(sql, args=(f"%{s_name}%",))
    return render(request, "billList.html", {"data": data, "sup": sup})
