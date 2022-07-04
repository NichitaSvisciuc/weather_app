from django.db import models
from django.contrib.auth.models import User


class UserSubscribtionProfile(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	subscription = models.ForeignKey('Subscription', 
									related_name = 'users', 
									on_delete = models.SET_NULL, 
									null = True, 
									blank = True)

	is_subscribed = models.BooleanField(default = False)

	sub_start_date = models.DateField(auto_now = True, null = True, blank = True)
	sub_expiration_date = models.DateField(null = True, blank = True)

	def __str__(self):

		if self.is_subscribed == False:
			return f'{self.user.username} is not subscribed'

		return f'{self.user.username} subscribed to subscription {self.subscription.subscription_type}'


class Subscription(models.Model):

	subscription_type = models.CharField(max_length = 200)
	price = models.IntegerField(default = 1)

	def __str__(self):
		return f'{self.subscription_type} : {self.price}'
