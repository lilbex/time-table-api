from django.db import models
from .user import User
from .term import Term
import uuid

class Classe(models.Model):
    """
    Class Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.class_name