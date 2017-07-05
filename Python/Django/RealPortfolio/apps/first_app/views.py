from django.shortcuts import render

def index(request):
	return render(request, 'first_app/index.html')
def show(request):
	print request.method
	return render(request, 'first_app/projects.html')
def about(request):
	print request.method
	return render(request, 'first_app/about.html')
def testimonials(request):
	print request.method
	return render(request, 'first_app/testimonials.html')
