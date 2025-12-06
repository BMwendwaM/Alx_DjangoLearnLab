from django.shortcuts import render


# View for Post Model

def home(request):
    return render(request, 'blog/base.html')