import django


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "title":"about us",
        "my_text":"this is aboutt us",
        "my_number":1234,
        "html_text":"<h2>hello user</h2>",
        "my_list":[111.222,333,444,"about","ABC"]
    }
    return render(request, "about.html", my_context)

def settings_view(request,*args, **kwargs):
    return render(request, "settings.html", {})
