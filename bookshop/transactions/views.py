from django.shortcuts import render
from .form import AddMoneyForm
from accounts.models import UserBookAccount
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from post.models import Post
from accounts.models import PurchaseModel


@login_required
def addMoney(request):
    form = AddMoneyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        amount = form.cleaned_data['amount']

        user_account = UserBookAccount.objects.get(user=request.user)
        user_account.balance += amount
        user_account.save()

        return render(request, 'home')

    return render(request, 'addMoney.html', {'form': form})


class BuyBookView(View):
    def get(self, request, id):
        book = get_object_or_404(Post, pk=id)
        user_account = request.user.account
        user = user_account.user
        if user_account.balance >= book.price:
            user_account.balance -= book.price
            user_account.save()
            book.save()
            purchase = PurchaseModel.objects.create(
                user=request.user, book=book)
            purchase.save()
            return render(request, 'home', {'book': book})

        else:
            return redirect('home')
