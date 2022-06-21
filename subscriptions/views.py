from django.shortcuts import get_object_or_404, redirect, render

from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import *

def add_subscription(request, sub_id = None):

	if request.method == 'POST':

		subscription_id = request.POST.get('subscription_id')
		subscription = get_object_or_404(Subscription, id = subscription_id)

		user = request.user

		user.usersubscribeprofile.subscription = subscription
		user.usersubscribeprofile.is_subscribed = True
		user.usersubscribeprofile.sub_expiration_date = datetime.today() + relativedelta(months = 1)
		user.usersubscribeprofile.save()

		return redirect('main-page')

	else:

		subscription = get_object_or_404(Subscription, id = sub_id)

		return render(request, 'perform_payment.html', {'subscription' : subscription})