from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    """Define user information"""

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = "کاربر ها"

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # for use default user django
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    # username = models.CharField('username', max_length=50, null=True, blank=True, primary_key=True)
    username = models.CharField('username', max_length=50, unique=True)
    # profile = models.TextField('description', max_length=150, null=False)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='F')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=50, null=True)
    country = models.CharField('country', max_length=20, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date', auto_now_add=True)
    update_date = models.DateTimeField('update date', auto_now=True)
    credit = models.IntegerField('credit', default=20)
    # friends = models.ManyToManyField("User", blank=True, related_name="friend")
    friends = models.ManyToManyField("Profile", blank=True, related_name="my_friends")

    @property
    def full_name(self):
        """This method returns the user's full name"""
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username} registered at {self.register_date}'

    def delete(self):
        """This method deleted the object/user"""
        deleted_obj = f'{self.first_name}_{self.last_name} object/user deleted'
        self.delete()
        return deleted_obj

    def update_credit(self, amount):
        """This method updates the user credentials."""
        self.credit += amount
        self.save()

    def get_friends(self):
        """return a list of user friend"""
        return self.friends.all()

    def get_friends_no(self):
        """return count of friend"""
        return self.friends.all().count()

    def get_books(self):
        """get all book of user"""
        # return self.user.all()
        return self.owner.all()

    def get_books_no(self):
        """get count all book of user"""
        # return self.user.all().count()
        return self.owner.all().count()


class Relationship(models.Model):
    """This method defined a relationship for a user"""
    STATUS_CHOICES = [('A', 'accepted'), ('R', 'requested'), ('N', 'name')]
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='N')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}, {self.receiver}, {self.status}'

# SocialNetworkBook command shell
# C:\1_venv_django\SocialNetworkBook>..\my_venv_django\Scripts\activate
# (my_venv_django) C:\1_venv_django\SocialNetworkBook>python manage.py shell
# >>> from user.models import User
# >>> parisa=User(first_name="parisa",last_name="etemadi",username="parisa74103",gender="F",
# phone_number="09010488477",biography="MSc",country="iran",website="parisa.ir",email="parisa@gmail.com")
# >>> parisa.save()
# >>> sara=User(first_name="sara",last_name="ghaneei",username="sara74103",gender="F",phone_number="090100000",
# biography="MSc",country="iran",website="sara.ir",email="sara@gmail.com")
# >>> sara.save()
# >>> zahra=User(first_name="zahra",last_name="matinfar",username="zahra74103",gender="F",phone_number="090111111",
# biography="MSc",country="iran",website="zahra.ir",email="zahra@gmail.com")
# >>> zahra.save()
# >>> elnaz=User(first_name="elnaz",last_name="etemadi",username="elnaz74103",gender="F",phone_number="09010488477",
# biography="MSc",country="iran",website="elnaz.ir",email="elnaz@gmail.com")
# >>> elnaz.save()
# >>> sara.friends.add(zahra)
# >>> sara.friends.all()
# <QuerySet [<User: zahra74103 registered at 2021-07-09 12:58:39.261273+00:00>]>
# >>> sara.friends.add(parisa)
# >>> sara.friends.all()
# <QuerySet [<User: parisa74103 registered at 2021-07-09 12:58:03.315138+00:00>, <User: zahra74103 registered
# at 2021-07-09 12:58:39.261273+00:00>]>
