from django.shortcuts import render
from .forms import InputForm, SnippetForm
import pywhatkit
import cgi


# Create your views here.
def home_view(request):

    if request.method == 'post':
        form = InputForm(request.post)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            Issue = form.cleaned_data['Issue']
            Description = form.cleaned_data['Description']
            covid_affected = form.cleaned_data['covid_affected']
            phone_no = form.cleaned_data['phone_no']
            print(name, email, Issue, Description, covid_affected, phone_no)

    form = InputForm()
    return render(request, "index.html", {'form': form})


def Snippet_detail(request):
    if request.method == 'post':
        form = SnippetForm(request.post)
        if form.is_valid():
            print(form.cleaned_data['name'])
    form = SnippetForm()
    return render(request, "base.html", {'form': form}, pywhatkit.sendwhatmsg_instantly('+91 8897139371','Greeting from CyGen,You have an appointment on 12-12-2022',10, True))
