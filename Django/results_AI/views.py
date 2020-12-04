from django.shortcuts import render

# Create your views here.
def results(request):
    return render(request, 'results_AI_index.html', {})