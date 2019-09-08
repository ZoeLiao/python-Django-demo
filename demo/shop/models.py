from django.db import models
from django.urls import reverse
import django.utils.timezone as timezone


class Category(models.Model):
    # db_index=True: 加索引
    name = models.CharField(
            max_length=200,
            db_index=True
        )
    slug = models.SlugField(
            max_length=200,
            db_index=True,
            unique=True
        )

    # 定義資料庫 
    class Meta:
        # 排序方式
        # ordering incurs a cost to your database
        ordering = ('name',)
        # 設置 models 直觀可讀的名稱
        verbose_name = 'catgory'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    # on_delete: 定義外來鍵和一對一關係時需要加，避免不一致問題
    #     - CASCADE: 級聯刪除（一般用這個） 
    #     - PROTECT: 會報完整性錯誤
    #     - SET_NULL: 將外來鍵設為 null，前提是可為 null
    #     - SET_DEFAULT: 設定=外來鍵的預設值
    #     - SET(): 呼叫外面的值
    category = models.ForeignKey(
            Category,
            related_name='products',
            on_delete=models.CASCADE  
        )
    name = models.CharField(
            max_length=200,
            db_index=True
        )
    slug = models.SlugField(
            max_length=200,
            db_index=True
        )
    image = models.ImageField(
            upload_to='products/%Y/%m/%d',
            blank=True
        )
    description = models.TextField(blank=True)
    # 不用 FloatField 以避免精度問題
    price = models.DecimalField(
            max_digits=10,
            decimal_places=2
        )
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    # 希望第一次生成時間又可以更改：
    # 1. auto_now_add=True: 第一次保存時生成的時間，之後修改不會更新，所以不能用
    # available = models.DateTimeField(
    #        auto_now_add=True
    #    )
    # 
    # 2. 將 default 設置為當前時間，之後可以修改
    created_at = models.DateTimeField(
            default = timezone.now
        )
    # auto_now=True: 每次修改時，改為最新時間 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        # 用兩個字段查尋
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

