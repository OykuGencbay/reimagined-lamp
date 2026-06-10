from django.shortcuts import render
def home(request):
    return render(request, "pages/home.html", {
        "title": "Company Name | Professional Services",
        "description": "Company description here.",
    })
def about(request):
    return render(request, "pages/about.html", {
        "title": "About Us | Company Name",
        "description": "Learn about our company, mission, and services.",
    })
def services(request):
    return render(request, "pages/services.html", {
        "title": "Our Services | Company Name",
        "description": "Explore the professional services offered by Company Name.",
    })
def contact(request):
    return render(request, "pages/contact.html", {
        "title": "Contact Us | Company Name",
        "description": "Contact Company Name for professional services, support, and business inquiries.",
    })