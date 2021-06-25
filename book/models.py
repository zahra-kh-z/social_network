from django.db import models
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    """Definition of book authors by name"""
    name = models.CharField('name', max_length=30)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    """Define book information"""
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = "کتاب ها"

    STATUS = [('F', 'Free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('Book name', max_length=100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publish_year = models.IntegerField('year of book publish', null=True)
    record_date = models.DateField('Time to record book', null=True)
    update_time = models.DateTimeField('update time Book information', default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS, default="F")

    # # How to use DateTimeField for this fields
    # publish_year = models.DateTimeField('year of book publish', default=timezone.now())
    # publish_year = models.DateTimeField('year of book publish', auto_now_add=True)
    # record_date = models.DateTimeField('Time to record book', null=True, auto_now_add=True)

    @property
    def book_author(self):
        """This method returns the name and author of the book"""
        return f'{self.name} {self.author}'

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
