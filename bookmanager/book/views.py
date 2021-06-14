import os

import math
from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
# Create your views here.


def bookList(request):

    # 添加数据
    book = BookInfo(
        name='python',
        pub_date='2020-1-1'
    )
    book.save()

    # 方式二
    BookInfo.objects.create(
        name='java',
        pub_date='2020-1-1'
    )

    # 更新数据
    BookInfo.objects.filter(id=1).update(
        comment_count=200,
        read_count=100
    )

    # 删除数据
    # 方式一
    BookInfo.objects.filter(id=6).delete()
    # 方式二
    book = BookInfo.objects.get(id=6)
    book.delete()
    # 查询包含'湖'的图书
    BookInfo.objects.filter(name__contains='湖')
    # 查询义'部'结尾的图书
    BookInfo.objects.filter(name__endswith='部')
    # 查询书名为空的图书
    BookInfo.objects.filter(name__isnull=True)
    # 查询编号为1,3或5的图书
    BookInfo.objects.filter(id__in=[1, 3, 5])
    # 查询id大于3的图书
    BookInfo.objects.filter(id__gt=3)
    # 查询id不为3的图书
    BookInfo.objects.exclude(id=3)
    # 查询1980年发表的图书
    BookInfo.objects.filter(pub_date__year='1980')
    # 查询1990年1月1日后发表的图书
    BookInfo.objects.filter(pub_date__gt='1990-1-1')

    from django.db.models import F, Q

    # 需要查询id大于2 并且阅读量大于20的书籍
    BookInfo.objects.filter(id__gt=2, read_count__gt=20)
    # 查询阅读量大于等于评论量的图书
    BookInfo.objects.filter(read_count__gt=F('comment_count'))
    # 查询阅读量大于等于评论量2倍的图书
    BookInfo.objects.filter(read_count__gt=F('comment_count')*2)
    # 需要查询id大于2 或者 阅读量大于20的书籍
    BookInfo.objects.filter(Q(id__gt=2) | Q(comment_count__gt=20))

    # 查询书籍id不为3
    BookInfo.objects.exclude(id=3)
    BookInfo.objects.filter(~Q(id=3))

    from django.db.models import Sum, Avg, Max, Min, Count
    # 当前数据的阅读总量
    BookInfo.objects.aggregate(Sum('read_count'))

    # 排序
    BookInfo.objects.all().order_by('read_count')
    # 倒序
    BookInfo.objects.all().order_by('-read_count')

    # 查询书籍为1的所有人物信息
    book = BookInfo.objects.get(id=1)
    book.peopleinfo_set.all()
    # 通过书籍 查询人物
    person = PeopleInfo.objects.get(id=1)
    person.book.name

    # 查询图书，要求图书人物为"郭靖"
    # 查询图书，要求图书中人物的描述包含"八"
    BookInfo.objects.filter(peopleinfo__name='郭靖')
    BookInfo.objects.filter(peopleinfo__description__contains='八')

    # 查询书名为“天龙八部”的所有人物
    # 查询图书阅读量大于50的所有人物

    PeopleInfo.objects.filter(book__name='天龙八部')
    PeopleInfo.objects.filter(book__read_count__gt=50)