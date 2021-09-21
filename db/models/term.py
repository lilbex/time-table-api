from django.db import models
import uuid

class Term(models.Model):
  """Term model."""
  id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=200)
  periods_per_day=models.IntegerField(default=0)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.name