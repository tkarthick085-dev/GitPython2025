from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sample(request):
    msg="This is my first application"
    return HttpResponse(msg)

def django(request):
    msg="This is my first django application"
    return HttpResponse(msg)

def homePage(request):
    msg = """<html>
        <head>
        <title>HomePage</title>
        </head>
        <body>
        <h1>This is a HomePage</h1>
        <a href="/login">Login</a>
        <a href="/register">Register</a>
        <a href="/payment ">Payment</a>
        </body>
        </html>"""

    return HttpResponse(msg)

def loginPage(request):

    return HttpResponse("""<html>
    <head>
    <title>LoginPage</title>
    </head>
    <body>
    <h1>This is a LoginPage</h1>
    </body>
    </html>""")

def registerPage(request):

    return HttpResponse("""<html>
    <head>
    <title>RegistrationPage</title>
    </head>
    <body>
    <h1>This is a RegistrationPage</h1>
    </body>
    </html>""")

def paymentPage(request):

    return HttpResponse("""<html>
    <head>
    <title>PaymentPage</title>
    </head>
    <body>
    <h1>This is a PaymentPage</h1>
    </body>
    </html>""")