from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class User(AbstractUser):
    GENDER_CHOISES = (
        ('Male','male'),
        ('Female','female')
    )
    username = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True
    )
    phone_number = models.CharField(
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    middle_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    password = models.CharField(
        max_length=255
    )
    is_verified = models.BooleanField(
        default=False
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOISES,null=True)

    @classmethod
    def create_user(cls,phone_number,password,**extra_fields):
        user:cls = cls.objects.filter(phone_number=phone_number)
        if user:
            return 'This phone number is busy!'
        else:
            user = User.objects.create(
                phone_number=phone_number,
                password=password
            )
            user.set_password(password)
            user.save()
            return user

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username','email']
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        elif self.username:
            return self.username
        else:
            return self.phone_number or 'nul'



class Verification(models.Model):
    code = models.IntegerField(unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def code_generate(cls,user):
        new_code = random.randint(10000,100000)

        while cls.objects.filter(code=new_code):
            new_code = random.randint(10000, 100000)
        obj = cls.objects.create(
            code=new_code,
            user=user
        )
        return obj


