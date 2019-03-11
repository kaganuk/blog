from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})