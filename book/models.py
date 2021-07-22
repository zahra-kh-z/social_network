from django.db import models
from django.utils import timezone
from user.models import Profile


# Create your models here.
class Book(models.Model):
    """Define book information"""

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = "کتاب ها"

    STATUS = [('F', 'Free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('Book name', max_length=100, null=True, blank=True)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publish_year = models.IntegerField('year of book publish', null=True)
    image = models.ImageField(upload_to='books/', blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="owner")
    liked = models.ManyToManyField(Profile, blank=True, related_name="likes")
    status = models.CharField(max_length=1, choices=STATUS, default="F")
    created = models.DateField('Time to record book', null=True)
    updated = models.DateTimeField('update time Book information', default=timezone.now)

    # # How to use DateTimeField for this fields
    # publish_year = models.DateTimeField('year of book publish', default=timezone.now())
    # publish_year = models.DateTimeField('year of book publish', auto_now_add=True)
    # record_date = models.DateTimeField('Time to record book', null=True, auto_now_add=True)

    @property
    def book_author(self):
        """This method returns the name and author of the book"""
        # return f'{self.name} {self.author}'
        return f'{self.name} {self.status}'

    def __str__(self):
        return f'{self.name} : status is {self.status}'

    def change_status(self):
        """
        This method determines the status of each book
        F is Free, B is borrowed, D is deprecated
        """
        if self.status == 'F':
            self.status = 'B'
        else:
            self.status = 'F'
        self.save()
        return self.status

    def get_publish_year(self):
        return self.publish_year.year


class Comment(models.Model):
    """set a comment for a book"""

    class Meta:
        ordering = ('-created',)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """set a like for book"""
    LIKE_CHOICE = [('L', 'like'), ('D', 'dislike')]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='like_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.CharField(max_length=3, choices=LIKE_CHOICE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def toggle(self):
        """status for like/dislike """
        if self.like == 'L':
            self.like = 'D'
        else:
            self.like = 'L'
        self.save()

# class Author(models.Model):
#     """Definition of book authors by name"""
#     name = models.CharField('name', max_length=30)
#
#     def __str__(self):
#         return f'{self.name}'

# # python console, how to create object by models
# from book.models import Book, Author
# # create object by models
# A1 = Author(name='ali')
# A1.name  # 'ali'
# A2 = Author.objects.create(name='sara')
# A2.name  # 'sara'
# x = Author.objects.all()
# x  # <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
# B1 = Book('happy', A1, '2000', '2020', '2020', 'Free')
# B1.name  # <Author: Author object (None)>
# from datetime import date
# B2 = Book('happy', A1, date(2005, 7, 27), date(2005, 7, 27), date(2005, 7, 27), 'Free')
# B2.name  # <Author: Author object (None)>
# B2 = Book(name='happy', author=A1, publish_year=date(2005, 7, 27), record_date=date(2005, 7, 27),
#           update_time=date(2005, 7, 27), status='Free')
# B2.name  # 'happy'
# B2.author  # <Author: Author object (None)>
# B2.author.name  # 'ali'
# B3 = Book(name='computer', author=A1, publish_year=date(2005, 7, 27), record_date=date(2005, 7, 27),
#           update_time=date(2005, 7, 27), status='Free')
# B3.name  # 'computer'
# A1.save()
# B4 = Book(name='computer', author=A1, publish_year=2005, record_date=date(2005, 7, 27), update_time=date(2005, 7, 27),
#           status='Free')
# B4.save()
# A1.book_set.all()  # <QuerySet [<Book: computer and 2005-07-27 00:00:00+00:00>]>
# A1.book_set.get()  # <Book: computer and 2005-07-27 00:00:00+00:00>
