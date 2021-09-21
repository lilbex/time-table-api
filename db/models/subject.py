from django.db import models
from .user import User
from .term import Term
from .classe import Classe
import uuid

class Subject(models.Model):
    """
    Subject Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classe, on_delete=models.CASCADE)
    time_per_week = models.IntegerField(default=0)
    

    def __str__(self):
        return self.subject_name