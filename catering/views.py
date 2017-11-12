from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from product.models import Catering, ProductImage
from catering.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError


class cateringView(TemplateView):
    template_name = 'catering/index.html'

    def get_context_data(self, **kwargs):
        context = {}

        return context


class cateringView(generic.View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'catering/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            details = form.cleaned_data['details']

            fullMessage = "<html><body>" \
                          "<p>Email From: {name}</p>" \
                          "<hr>" \
                          "<p>Subject: {subject}</p>" \
                          "<p>{details}</p>" \
                          "<p>Name: {name}</p>" \
                          "</body></html>".format(name=name, subject=subject, details=details, phone=phone)

            form.save()
            try:
                send_mail("Email From Ararat 17", fullMessage, name, ["info@ararat17.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(request, self.template_name)

        return render(request, self.template_name, {'form': form})


