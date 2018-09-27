from django.shortcuts import render
from django.views.generic.base import TemplateView


class SearchResultView(TemplateView):
    template_name = 'baidu/index.html'

    def get(self, request):

        return render(request, self.template_name)

