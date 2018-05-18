from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    # Set 121 relationship
    user = models.OneToOneField(User, on_delete=True)

    # Additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # define what will be shown when coder print model
    def __str__(self):
        return self.user.username

