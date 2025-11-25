from django.shortcuts import render
from django.http import HttpResponse

# Simple view that returns plain text in the browser
def hello(request):
    return HttpResponse("Hello Django! My first page.")

# View for the home/index page
def indexpage(request):
    context = {}   # Empty context for GET request (first load)

    # Check if user submitted the form (POST request)
    if request.method == "POST":
        # Getting form input values
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')

        # Passing form data to template
        context = {
            'student': {
                'name': name,
                'age': age,
                'city': city
            }
        }

    # Render the HTML template with context data
    return render(request, 'Dapplication/index.html', context)

# View for about page with static data
def about(request):
    context = {
        'Name': 'Daizy',
        'city': 'Mumbai',
        'age': 22
    }
    return render(request, 'Dapplication/about.html', context)

# Dynamic URL view: takes ID from URL and displays it
def showStu(request, id):
    return HttpResponse(f"Student ID is {id}")
