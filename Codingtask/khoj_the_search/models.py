from django.db import models
from AutenticationApp.models import User

class InputValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
