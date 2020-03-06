from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name = "invitations_sent")
    to_user = models.ForeignKey(
        User,
        related_name="invitations_received",
        verbose_name="User to invite",
        help_text="Please select the user you want to play the game with.",
        on_delete=models.CASCADE
    )

    message = models.CharField(
        max_length=300,
        verbose_name="Optional Message",
        help_text="Its always nice to add a friendly message"
    )
