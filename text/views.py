from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index (request):
    return render(request, 'index.html' )
def Analyze(request):
    # To Get the text
    djtext = request.POST.get('text',"Default")

    # To Analize Text 
    fullcaps  = request.POST.get('fullcaps',"off")
    RemovePunc = request.POST.get('RemovePunc',"off")
    Removenewline = request.POST.get('Removenewline',"off")
    Removeextraspace = request.POST.get('Removeextraspace',"off")
    Counter = request.POST.get('Counter',"off")
    
    #Check Boxes

    if (RemovePunc == 'on'):
        Analyzed = ""
        punctuations = '''!()-_[]{}"'\@#$%^&*?/|`~;'''
        for i in djtext:
            if i  not in punctuations:
                Analyzed = Analyzed + i
        params = {'purpos':'Punctuations Removed', 'Analized_Text':Analyzed}
        djtext = Analyzed
    if fullcaps == 'on':
        Analyzed = ""
        for char in djtext:
            Analyzed = Analyzed + char.upper()
        params = {'purpos':'Capitalaized', 'Analized_Text':Analyzed}
        djtext = Analyzed
    if (Removenewline == 'on'):
        Analyzed = ""
        for i in djtext:
            if i !="\n" and i != "\r" :
                Analyzed = Analyzed + i
        params = {'purpos':'All New Lines Removed', 'Analized_Text':Analyzed}
        djtext = Analyzed
    if (Removeextraspace == 'on'):
        Analyzed = ""
        for i, char in enumerate(djtext):
            if  djtext[i] ==" " and djtext[i+1] == " ":
                pass
            else:
                Analyzed = Analyzed + char
        params = {'purpos':'Spaces Removed', 'Analized_Text':Analyzed}
        djtext = Analyzed
    if (Counter == 'on'):
        Analyzed = ""
        i = 1
        for i,char in enumerate(djtext):
            charCounter = i+1 
            params = {'purpos':'Charactors Counted', 'Analized_Text':charCounter}
            djtext = Analyzed
    if(RemovePunc!="on" and Removenewline!="on" and Removeextraspace!="on" and Counter!="on" and fullcaps!="on"):
       return HttpResponse("Error")

    return render(request, 'Analyze.html', params)