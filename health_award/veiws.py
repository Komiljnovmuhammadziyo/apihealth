from django.shortcuts import render
from django.views import View


class landing_page(View):
    def get(self, request):

        return render(request, template_name='home.html')
