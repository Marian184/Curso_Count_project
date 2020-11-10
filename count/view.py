from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'key1':'Ok This is the value of Key1'})

def eggs(request):
    return HttpResponse('<h1>This is Test </h1> ')

def count(request):
    fulltext = request.GET['fulltext']

    words = fulltext.split()
    dic={}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    # cont=0
    # didi={'word':0}
    # for i in fulltext:
    #     if i !=' ':
    #         cont+=1
    #         didi[word] +=1
    dictsorted = sorted(dic.items(), key =operator.itemgetter(1), reverse= False)

    return render(request,'count.html',{'fulltext':fulltext,'counting':len(words),'dictsorted':dictsorted})

def about(request):
    return render(request,'about.html')