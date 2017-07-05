from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, ('first_app/index.html'))

# def process(request):
#     request.session['full_name'] = request.POST["full_name"]
#     request.session['location'] = request.POST["location"]
#     request.session['language'] = request.POST["language"]
#     request.session['comments'] = request.POST["comments"]
#
#     if not 'count' in request.session:
#         request.session['count'] = 1
#     else:
#         request.session['count'] += 1
#
#     return redirect('/result')
#
# def result(request):
#
#     return render(request, ('first_app/results.html'))
