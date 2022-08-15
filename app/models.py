from django.db import models
from django.contrib.auth.models import User
from random import randrange
from string import ascii_uppercase
from .views import MAIN_URL
# Create your models here.


class Link (models.Model) :
    user = models.ForeignKey(User, related_name='user_link',on_delete=models.CASCADE)
    link = models.URLField()
    hash_code = models.CharField(max_length=100)
    visitors = models.IntegerField(default=0)

    def __str__(self) :
        return f'{self.user} -> {self.hash_code}'

    def create_link (user, link) :
        key = []
        num = 0
        while True :
            num = num + 1
            for i in range(num):key.append(ascii_uppercase[randrange(0,len(ascii_uppercase))])
            my_has_code = ''.join(key)
            if Link.objects.filter(hash_code=my_has_code).exists():
                pass
            else :
                break
        
        if 'https' in link :
            pass
        else :
            link = f'https://{link}'
        Link.objects.create(
            user=user,
            link=link,
            hash_code=my_has_code
        )



        


# www.facebook.com -> /ADQ