from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import html
import re

def members(request):
    return HttpResponse("Hello world!")

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        search_term = request.POST.get('username')
        if detect_xss(search_term) or detect_sql_injection(search_term):
            return render(request,'home.html')
        else:
            return render(request, 'success.html', {'search_term': search_term})

@csrf_exempt
def submitPassword(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        password = request.POST.get('Password')
        if validate_common_password(password):
            return render(request, 'successPass.html', {'password': password})
        else:
            return render(request,'home.html')

def protect_against_xss(user_input):
    """Escape special characters in user input to prevent XSS attacks."""
    return html.escape(user_input)

def detect_xss(user_input):
    """Check for potential XSS in user input."""
    return '<script>' in user_input

def detect_sql_injection(user_input):
    # Common SQL injection patterns
    sql_injection_patterns = [
        r'\bSELECT\b.*\bFROM\b',
        r'\bINSERT\b.*\bINTO\b',
        r'\bUPDATE\b.*\bSET\b',
        r'\bDELETE\b.*\bFROM\b',
        r'\bUNION\b.*\bSELECT\b',
        r'\bOR\b.*\b1=1\b',
        # Add more patterns as needed
    ]

    for pattern in sql_injection_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True

    return False

def validate_common_password(value):
    with open('10-million-password-list-top-1000000.txt', 'r') as common_passwords_file:
        common_passwords = [line.strip() for line in common_passwords_file]

    return value not in common_passwords
# Create your views here.

