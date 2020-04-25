from django.db import models


class Tutor(models.Model):
    t_title = models.CharField(max_length=120)
    t_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.t_content) >= 50:
            return self.t_content[:50] + '...'
        else:
            return self.t_content


class Ranking(models.Model):
    r_user = models.CharField(max_length=16)
    r_rank = models.CharField(max_length=16)
    r_no = models.IntegerField()

    def __str__(self):
        return self.r_user + '\t' + self.r_rank + '\t' + str(self.r_no)


class UserInfo(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_pwd = models.CharField(max_length=256)
    u_email = models.CharField(max_length=128, default='example@outlook.com')
    u_img = models.ImageField(upload_to='icons/%Y/%m/%d/')
    u_response = models.IntegerField(default=0)
    u_fans = models.IntegerField(default=0)


class PersonInfo(models.Model):
    person = models.OneToOneField(UserInfo, on_delete=models.CASCADE, blank=True, null=True)
    p_name = models.CharField(max_length=16, blank=True, null=True)
    p_age = models.IntegerField(blank=True, null=True)
    p_sex = models.BooleanField(blank=True, null=True)
    p_tel = models.CharField(max_length=11, blank=True, null=True)
    p_intro = models.TextField(blank=True, null=True)


class Strategy(models.Model):
    strategy = models.ForeignKey(UserInfo, on_delete=models.CASCADE, blank=True, null=True)
    s_title = models.CharField(max_length=128)
    s_content = models.TextField()
    s_words = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


class Remark(models.Model):
    u_remark = models.ForeignKey(UserInfo, on_delete=models.CASCADE, blank=True, null=True)
    s_remark = models.ForeignKey(Strategy, on_delete=models.CASCADE, blank=True, null=True)
    r_name = models.CharField(max_length=128, default='Bleurenard')
    r_content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
