from django.db import models
from django.utils import timezone
from accounts.models import Profile
from polymorphic.models import PolymorphicModel
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.

class Tobacco(PolymorphicModel):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/img', blank=True, null=True)
    thumbnail = ThumbnailerImageField(upload_to='media/cigarette', blank=True)
    price = models.CharField(max_length=10)
    rel_date = models.CharField(max_length=20, blank=True)
    nicotine =  models.FloatField()
    TAR = models.FloatField()
    feel_of_hit = models.CharField(max_length=10)
    score = models.FloatField(default=0)
    total_like = models.PositiveIntegerField(default=0)
    like_user = models.ManyToManyField(Profile)

    def __str__(self):
        return self.brand+self.name

    class Meta:
        ordering = ['-rel_date']

class Cigarettes(Tobacco):
    is_local = models.BooleanField()
    is_menthol = models.BooleanField()

class ElecCigarettes(Tobacco):
    c_type = models.CharField(max_length=20)

class Comment(models.Model):
    belongs_to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    belongs_to_tobacco = models.ForeignKey(Tobacco, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    feel_of_hit = models.CharField(max_length=10)
    score = models.PositiveIntegerField(default=3)
    content = models.TextField()

class Request(models.Model):
    is_elec = models.BooleanField()
    is_added = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    rel_date = models.CharField(max_length=20, blank=True)
    nicotine =  models.FloatField(blank=True)
    TAR = models.FloatField(blank=True)
from django.db import models
from django.utils import timezone
from accounts.models import Profile
from polymorphic.models import PolymorphicModel

# Create your models here.

class Tobacco(PolymorphicModel):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    rel_date = models.CharField(max_length=20, blank=True)
    nicotine =  models.FloatField()
    TAR = models.FloatField()
    feel_of_hit = models.CharField(max_length=10, default='중')
    score = models.FloatField(default=0)
    total_like = models.PositiveIntegerField(default=0)
    like_user = models.ManyToManyField(Profile)

    def __str__(self):
        return self.brand+self.name

    class Meta:
        ordering = ['-rel_date']

class Cigarettes(Tobacco):
    is_local = models.BooleanField()
    is_menthol = models.BooleanField(default=False)

class ElecCigarettes(Tobacco):
    c_type = models.CharField(max_length=20)

class Comment(models.Model):
    belongs_to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    belongs_to_tobacco = models.ForeignKey(Tobacco, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    feel_of_hit = models.CharField(max_length=10)
    score = models.PositiveIntegerField(default=3)
    content = models.TextField()

class Request(models.Model):
    is_elec = models.BooleanField(default=False)
    is_added = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    rel_date = models.CharField(max_length=20, blank=True)
    nicotine =  models.FloatField(blank=True)
    TAR = models.FloatField(blank=True)
    is_menthol = models.BooleanField(blank=True)