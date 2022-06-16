from django.views.generic import View
from mobiles.forms import MobileCreateForm
from django.shortcuts import render,redirect
from django.contrib import messages
from mobiles.models import Mobile


class MobileCreateView(View):
    form_class=MobileCreateForm
    def get(self,request,*args,**kwargs):
        return render(request,"add-mobile.html",{"form":self.form_class()})
    def post(self,request,*args,**kwargs):
        form=MobileCreateForm(request.POST)
        if form.is_valid():
            Mobile.objects.create(
                mobile_id=form.cleaned_data.get("mobile_id"),
                mobile_name=form.cleaned_data.get("mobile_name"),
                brand=form.cleaned_data.get("brand"),
                price=form.cleaned_data.get("price"),
                network=form.cleaned_data.get("network"),)
            messages.success(request,"phone added successfully")
            return redirect("add-mobile")
        else:
            messages.error(request, "phone cannot be added")
            return render(request, "add-mobile.html", {"form": self.form_class()})
