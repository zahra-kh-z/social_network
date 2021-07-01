from django.db import models


# Create your models here.
class User(models.Model):
    """Define user information"""

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = "کاربر ها"

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
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
    update_date = models.DateTimeField('update date')
    credit = models.IntegerField('credit', default=20)
    friends = models.ManyToManyField("User", blank=True, related_name="friend")

    @property
    def full_name(self):
        """This method returns the user's full name"""
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username} registered at {self.register_date}'

    def delete(self):
        """This method deleted the object/user """
        deleted_obj = f'{self.first_name}_{self.last_name} object/user deleted'
        self.delete()
        return deleted_obj

    def update_credit(self, amount):
        """This method updates the user credentials."""
        self.credit += amount
        self.save()


class Relationship(models.Model):
    """This method defined a relationship for a user """
    STATUS_CHOICES = [('A', 'accepted'), ('R', 'requested'), ('N', 'name')]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='N')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}, {self.receiver}, {self.status}'
