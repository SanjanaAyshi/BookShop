from django.db import models
# from accounts.models import UserBookAccount
# # Create your models here.


# class Transaction(models.Model):
#     # ekjon user er multiple transactions hote pare
#     account = models.ForeignKey(
#         UserBookAccount, related_name='transactions', on_delete=models.CASCADE)

#     amount = models.DecimalField(decimal_places=2, max_digits=12)
#     balance_after_transaction = models.DecimalField(
#         decimal_places=2, max_digits=12)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['timestamp']
