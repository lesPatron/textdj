from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello world</h1><br><a href='about/'>About section</a><br><a href='information/'>Information</a>")

def about(request):
    return HttpResponse("<h2>This is about</h2> <br> <a href ='/'>Go back</a>")

def information(request):
    parameter = {'name': 'rito', 'place':'howrah'}
    return render(request,'index.html', parameter)

def analyse(request):
    input_txt = request.POST.get('text','default')
    input_bool = request.POST.get('check','off')
    print(input_txt)
    print(input_bool)
    punc = list(''',.{""}:;''')
    output = ""
    if(input_bool != 'off'):
        for i in input_txt:
            if i not in punc:
                output+=i
        itr=""
        for j in output:
            if(j != '\n' and j !='\r'):
                itr+= j
        output = itr

    else:
        return HttpResponse("Invalid response bitch!")
    print(output)
    out = {'output':output}
    return render(request, 'analyse.html',out)