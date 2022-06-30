from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=200,
    help_text='enter a book genre (e.g. Science Fiction,French poetry,Egnlish, German History etc)')

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=200,
    help_text="Enter the books's natural language (e.g. English,French,Jpaanese,etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    summary=models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    isbn=models.CharField('ISBN',max_length=13,
    help_text='13 character')
    genre=models.ManyToManyField(Genre,help_text='Enter a brief description of the book')
    language=models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)
    total_copies=models.IntegerField()
    pic=models.ImageField(blank=True,null=True, upload_to='book_image')

    def __str__(self):
        return self.title


class Student(models.Model):
    roll_no=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=5)
    contact_no=models.CharField(max_length=10)
    total_book_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    pic=models.ImageField(blank=True,upload_to='profile_image')

    def __str__(self):
        return str(self.roll_no)


class Borrower(models.Model):
    student=models.ForeignKey('Student',on_delete=models.CASCADE)
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    issue_date=models.DateTimeField(null=True,blank=True)
    retrun_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.student.name + "borrowed" +self.book.title

class Reviews(models.Model):
    review=models.CharField(max_length=100,default='none')
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    student=models.ForeignKey('Student',on_delete=models.CASCADE)
    CHOICE=(
        ('0','0'),
        ('.5','.5'),
        ('1','1'),
        ('1.5','1.5'),
        ('2','2'),
        ('2.5','2.5'),
        ('3','3'),
        ('3.5','3.5'),
        ('4','4'),
        ('4.5','4.5'),
        ('5','5'),
        
    )
    rating=models.CharField(max_length=3,choices=CHOICE,default=2)


