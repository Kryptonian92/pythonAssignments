from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "hello!"
    request.session['sessionvar'] = "Hello Again!"
    context = {
        "stuff" : [1,2,3,4],
        "party" : ['baloons'],

    }
    return render(request, "superapp_templates/index.html")

def index2(request):
    print "hello 2!"
    return render(request, "supperapp_tempates/index.html")
