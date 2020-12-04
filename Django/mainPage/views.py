from django.shortcuts import render

def main(request):
    # return render(request, 'test.html', {})
    return render(request, 'mainPage_index.html', {})