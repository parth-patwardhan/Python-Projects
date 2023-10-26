from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book_name = models.CharField(max_length=180)
    book_author = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
    
