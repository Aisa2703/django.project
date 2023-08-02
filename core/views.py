from django.shortcuts import render, HttpResponse


def Homepage(request):
    return HttpResponse('HelloWorld!')


def Contacts(request):
    return HttpResponse('Contacts')


def About_Us(request):
    return HttpResponse('About_Us')


