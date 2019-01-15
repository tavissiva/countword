from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse('<h1>HELLO SIVA THIS IS YOUR FIRST WEBSITE KEEP ROCKING</h2>')
    return render(request, 'home.html')
#def site(request):
	#return HttpResponse('myfirstwebsite')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()
	print(wordlist)
   
	worddict={}
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
    

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict':worddict.items()})

def about(request):
	return render(request, 'about.html')