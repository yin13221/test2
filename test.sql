-- 超市管理表
create table t_supplier(
    id int primary key auto_increment,
    code varchar(20) comment '供应商编码',
    s_name varchar(100) comment '供用商名称',
    contacts varchar(100) comment '联系人',
    tel varchar(11) unique not null comment '联系电话',
    addr varchar(100) comment '联系地址',
    fax varchar(12) comment '传真 电话格式0373-*******',
    create_time datetime default CURRENT_TIMESTAMP comment '创建时间',
    s_desc varchar(200) comment '供应商描述'
);

create table t_bill(
    id int primary key auto_increment,
    code varchar(20) comment '订单编号',
    s_name varchar(100) comment '商品名称',
    unit varchar(20) comment '商品单位',
    num double comment '商品数量',
    price double comment '总金额',
    sup_name varchar(20) comment '供应商名字',
    state varchar(10) comment '是否付款',
    create_time datetime default CURRENT_TIMESTAMP comment '创建时间'
);

create table t_user(
    id int primary key auto_increment,
    code varchar(20) comment '用户编码',
    username varchar(100) comment '用户名称',
    password varchar(32) not null comment '密码',
    sex varchar(4) comment '性别',
    birth date comment '出生日期',
    tel varchar(11) unique not null comment '用户电话',
    addr varchar(100) comment '用户地址',
    s_type varchar(5) comment '用户类型'
);