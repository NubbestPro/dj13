from django.shortcuts import render

# Create your views here.
def home(request):
    wordcount = wordcount
    return render(request, "wordcount/count.html", {"wordcount":wordcount})