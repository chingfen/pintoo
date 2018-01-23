from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userProfile')
    name = models.CharField(max_length=128, blank=True, null=True) # 暱稱
    sex = models.CharField(max_length=128, blank=True, null=True) # 性別
    image = models.CharField(max_length=128, default='http://images.uncyc.org/zh-tw/3/32/Nobody%E9%A0%AD%E5%83%8F.jpg')
    birthdate = models.DateField(blank=True, null=True) # 生日
    introduction = models.TextField(blank=True, null=True) # *自我介紹
    lavel = models.FloatField() # 經驗
    emailVerifyCode = models.CharField(max_length=128) # Email驗證碼
    isEmailVerified = models.BooleanField(default=False) # Email驗證
    def __str__(self):
        return self.name + '(' + self.user.username + ')' + 'Lv.'+ str(int(self.lavel))
    
    
    