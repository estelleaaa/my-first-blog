from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):     # define model (it is an object) post is the mame of the model models.Model means that the post is a django model so django knows that it should be saved in the database.
    
     #def all properties(attributes), we need to define the type of each field(is it a number?a date?a relation to another object, like a user?)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # foreigKey is a link to another model.
    title = models.CharField(max_length=200)                    # charfield is how u define text with a limited number of characters.
    text = models.TextField()                                   #textfield is for a long text without a limit. 
    created_date = models.DateTimeField(default=timezone.now)   # datetimefield is a date and time 
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):                                          #define a function/method  publish is the name of the method.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title                                      #method often return sth/ here when we call __str__() we will get a text(string) with a post title.

