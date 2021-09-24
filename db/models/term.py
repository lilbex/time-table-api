from django.db import models
from .user import User
import uuid

class Term(models.Model):
  """Term model."""
  id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
  term_name = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  periods_per_day=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f'{self.id}'