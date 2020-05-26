

# 期末大作业

这是吴逸豪2018302180060、翁斌2018302180061的数据库期末大作业后端代码

## 功能介绍

整体代码实现了一个最简单线上论坛，具体功能包括：

1. 用户注册登录，用户信息上传，包含姓名、性别、工作、年龄、兴趣
2. 用户权限控制，在power字段储存，包括 0游客、1注册用户、2高级用户、3管理员、4开发者，权限依次扩大
3. 文章操作，包括创建、修改、删除基本操作，包含创建、修改时间记录，**并特色实现隐私发布功能**
4. 评论操作，包括创建、修改、删除、点赞操作，包含自动更新的创建、最近修改时间记录

具体实现见Mark 0.1部分

## 安全考量（突出特色）

本次大作业我们组结合专业特点，没有增加太多功能，而是将关注点放在安全方向。

大作业后端代码有两个版本 Mark 0.1为仅功能实现版本，Mark 0.2为考虑安全性后做出的改进版本，主要改进点有：

1. 将网络劫持及前端解包纳入考虑，采用加密传输与储存
2. 考虑SQL注入威胁，增加防注入措施
3. 使用 视图 和 角色 完善权限控制

具体见Mark 0.2部分

## 注意

本次数据库大作业使用 django 作为网络框架。

django 是十分优秀的适合文章类网站快速开发的十分优秀的网络框架，其本身具有隐藏SQL细节的数据库操作。

但为了展现课程所学知识，我们仅仅使用了django的路径导航部分（Urls部分），django的模型（Models）及视图（Views）部分也仅仅使用了与Urls连接的部分，数据库操作的主题使用的是python嵌入式sql，数据库使用Mysql完成。

# Mark 0.1

该版本仅为功能实现版本，接下来的功能实现细节将提前嵌入式sql中sql语句的简化版本，仅去除python中的字符串操作，方便老师与助教查看

## wx/test_app/views.py  登录部分

login: 
~~~mysql
select id,password from auther_user where name = username
~~~

从前端获取username、password，从数据库取出username相同的项的id、password，与获取的password对比，有匹配项说明已注册且密码正确，返回id



signup：
~~~mysql
INSERT INTO auther_user (`name`, `password`) 
VALUES (username,password);
~~~

从前端获取username、password，插入数据库用户表，支持同名用户，不考虑同名同密码用户

~~~mysql
select id,password from auther_user where name = username;
~~~

为实现注册后直接登录，在插入后紧接查询操作



userinfo：
~~~mysql
select * from auther_user where name = username;
~~~

从前端获取username，查询所有信息，并以字典json形式发回用户信息



userchange：

```mysql
update auther_user set name=%s,sex=%s,job=%s,age=%s,like=%s where id=%s;
,userinfo['name'], userinfo['sex'], userinfo['job'],userinfo['age'], userinfo['like'],id
```

通过id确定用户，从前端获取更改后的用户信息，并更新



userpowerup：

```mysql
select power from auther_user where id=userid;
update auther_user set power%s where id=userid;
,str(power+1)
```

通过userid确定用户，查询权限并加一修改，前端需要搭配认证系统，没有实现



## wx/article/views.py 文章部分

article_list：

```mysql
select * from article_post order by updated desc;
```

从数据库文章表中取出文章，以更新日期降序排序



article_Mylist：

```mysql
select * from article_post where author_id=userid order by updated desc;
```

从数据库文章表中取出特定用户文章，以更新日期降序排序



article_detail：

```mysql
select * from article_post where id=articleid
```

通过文章id确定文章，选出文章所有信息，加工后发回



article_create：

```mysql
insert into article_post(title,body,created,updated,author_id,privacy) values(%s,%s,%s,%s,%s,%s);
,value['title'], value['body'], value['updated'], value['created'], value['id'], value['privacy']
```

通过前端获取信息，插入新的文章记录



article_delete：

```mysql
delete from article_post where id=%s
```

通过前端发来的id确定文章，并删除



article_update：

```mysql
update article_post set title=%s,body=%s,privacy=%s,updated=%s where id=%s
```

通过前端发来的id确定文章，修改为前端提供的内容



## wx/answer/views.py 评论部分



commitAnswer：

```mysql
insert into answer_review(reviewText,writerID_id,questionID_id) values(%s,%s,%s)；
,request.POST.get("review"),request.POST.get("writerID"),request.POST.get("articleID")
```

前端传来文章id，评论者id，和评论内容，将其插入



addHelpful：

```mysql
update answer_review set helpfulVote=helpfulVote+1 where id=id
insert into answer_review_users_like(review_id,user_id) values(id，userid)
```

👍，更新两个表，文章点赞数 +- 1；添加某人对某评论的评价记录。此功能前端没有实现

取消👍同样在这个函数中

```mysql
update answer_review set helpfulVote=helpfulVote-1 where id=id
delete from answer_review_users_like where review_id=id and user_id=userid
```

文章点赞数-1，删除点赞记录



deleteAnswer：

```mysql
delete from answer_review where id=id
```

通过前端发来的id确定评论，删除评论



getAnswer：

```mysql
select * from answer_review where id=id
```

通过前端发来的id确定评论，获取评论的全体内容，选择性发回



getAnswerList：

```mysql
select * from answer_review where questionID_id=id
```

通过前端发来的id确定文章，获取文章下所有评论



# Mark 0.1 安全分析

Mark 0.1 为功能实现版，所有代码皆为最简单版本，因此存在各种各样的漏洞。主要有下面三种：

1. 控制信号在客户端明文储存，在网路中明文传输，很容易遭到拦截并修改。具体表现为用户id、文章id、评论id皆明文储存并传输，他们又在服务器中作为确定用户、文章、评论的控制信号。

   大体攻击流程为：

   1. 下载网页（web或使用解包软件解包（小程序、app）后获取服务器通讯地址
   2. 使用BurpSuite、Charles等皆可对本地运行的客户端进行抓包，并将各类id修改为想要攻击的
   3. 正常接收应答并显示，便可以实现越过登录验证的查看

   

2. 数据库及其操作未进行防注入操作，攻击者可轻易对数据库进行sql注入攻击

   大体攻击流程为：

   1. 下载网页（web或使用解包软件解包（小程序、app）后获取服务器通讯地址
   2. 通过接口设置及后续操作，猜测sql语句及数据库表名、属性名
   3. 使用模拟发包软件向返回数据的接口发送构造好的注入语句，如向article_Mylist接口发送id值 '1" or id < 2#' 便可以间接知道2号用户发了那些文章，导致隐私发送失效
   4. 使用union联合查找可得到注入更加危险的sql语句，实现查询任意数据，甚至直接操作数据库

   

3. 服务端明文储存所有信息，对用户隐私无保护



# Mark 0.2

针对Mark 0.1的安全分析，我们对后端代码进行了优化，主要有：

1. 

2. 
3.  
4. 