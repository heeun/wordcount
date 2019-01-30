from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for wordparameter in words:
        if wordparameter in word_dictionary:
            #increase
            word_dictionary[wordparameter]+=1
        else:
            #add to dictionary
            word_dictionary[wordparameter]=1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})   
