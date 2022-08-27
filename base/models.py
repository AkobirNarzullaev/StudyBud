from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(unique=True, null=True)
  bio = models.TextField(null=True)

  avatar = models.ImageField(null=True, default="avatar.svg")

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


class Topic(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,
                            null=True)  # By saying null=True we are allowing the database to be empty
  name = models.CharField(max_length=200)
  description = models.TextField(null=True,
                                 blank=True)  # By default null is set to true (it simply means it is allowed to be blank; null for the database and blank for the form)
  participants = models.ManyToManyField(User, related_name='participants', blank=True)
  updated = models.DateTimeField(
    auto_now=True)  # (auto_now = True) It simply means when the post is saved take a time stamp
  created = models.DateTimeField(auto_now_add=True)  # Takes a time stamp when a post is created

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.name


class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room,
                           on_delete=models.CASCADE)  # ForeignKey - many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option
  # when the parent is deleted CASCADE method deletes all the children
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.body[0:50]  # string slicing. first 50 characters will be displayed
