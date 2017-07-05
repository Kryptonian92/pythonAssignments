from django.shortcuts import render

# Create your views here.
def index(request):
    print "*"*50
    return render(request, 'first_app/index.html')
#
# The following is a list of commands from the Django Shell for creating and printing new Books
#
# (djangoEnv) Ausars-MBP:Books Ausar$ python manage.py shell
# Python 2.7.13 (default, Dec 17 2016, 23:03:43)
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from apps.first_app.models import Books
# >>> book = Books.objects.create(title="Life", author="Ausar", published_date = "2006-10-25", category = "Fiction")
# >>> Books.objects.create(title="Life", author="Ausar", published_date = "2006-10-25", category = "Fiction")
# <Books: Books object>
# >>> Books.objects.create(title="Tuples", author="Raf", published_date = "2006-10-25", category = "Fiction")
# <Books: Books object>
# >>> Books.objects.create(title="Tuples", author="Dictionaries", published_date = "2006-10-25", category = "Fiction")
# <Books: Books object>
# >>> Books.objects.all()
# <QuerySet [<Books: Books object>, <Books: Books object>, <Books: Books object>, <Books: Books object>]>
# >>> print Books.objects.all()
# <QuerySet [<Books: Books object>, <Books: Books object>, <Books: Books object>, <Books: Books object>]>
# >>> for i in Books:
# ...     print Books.title, Books.author, Books.publish_date
# ...
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: 'ModelBase' object is not iterable
# >>> text = Books.objects.create(title="Tuples", author="Dictionaries", published_date = "2006-10-25", category = "Fiction")
# >>> text = Books.objects.create(title="Tuples", author="Tuples", published_date = "2006-10-25", category = "Fiction")
# >>> text = Books.objects.create(title="Fiji Life", author="Claudia", published_date = "2006-10-25", category = "Fiction")
# >>> text
# <Books: Books object>
# >>> for i in text:
# ...     print i.title, i.author, i.category
# ...
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: 'Books' object is not iterable
# >>> new = Books.objects.all()
# >>> for i in new:
# ...     print i.title, i.author, i.category
# ...
# Life Ausar Fiction
# Life Ausar Fiction
# Tuples Raf Fiction
# Tuples Dictionaries Fiction
# Tuples Dictionaries Fiction
# Tuples Tuples Fiction
# Fiji Life Claudia Fiction
# >>> 
