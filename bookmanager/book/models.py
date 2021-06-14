from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # 准备书籍列表信息的模型类
    name = models.CharField(max_length=10, verbose_name='书名')
    pub_date = models.DateField(max_length=20, verbose_name='发布日期')
    read_count = models.IntegerField(default=0, verbose_name='阅读量')
    comment_count = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = "bookinfo"  # 指明数据库表名
        verbose_name = '图书'  # 在admin中显示站点名称

    def __str__(self):
        # 定义每个对象的显示信息
        return self.name


class PeopleInfo(models.Model):
    """人物列表信息的模型类"""
    GENDER_CHOICES = (
        (0,'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, verbose_name='描述')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

