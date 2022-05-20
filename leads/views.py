from multiprocessing import context
from pickletools import markobject
from django.shortcuts import redirect, render
from django.http import HttpResponse
from leads.forms.forms import LeadForm,LeadModelForm
from leads.models import Lead,Agent

# Create your views here.
def lead_list(request):
   lead = Lead.objects.all()
   context = {
     "lead":lead
   }
   return render(request,"lead_list.html",context)

def lead_detail(request,pk):
   lead =  Lead.objects.get(id=pk)
   context = {
      "lead":lead
   }
  
   return render(request,"lead_detail.html",context)

def lead_create(request):
   form = LeadModelForm()
   if request.method == "POST":
      form = LeadModelForm(request.POST)
      if form.is_valid():
         form.save()
         # first_name = form.cleaned_data['first_name']
         # last_name= form.cleaned_data['last_name']
         # age = form.cleaned_data['age']
         # agent = form.cleaned_data['agent']

         # Lead.objects.create(
         #    first_name = first_name,
         #    last_name = last_name,
         #    age = age,
         #    agent = agent,
         # )
         return redirect("/leads")
   context = {
      "form":form       
   }
   return render(request,"lead_create.html",context)

def lead_update(request,pk):
   lead = Lead.objects.get(id=pk)
   form = LeadModelForm(instance=lead)

   if request.method == "POST":
      form = LeadModelForm(request.POST,instance=lead)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "form":form,
      "lead":lead
   }
   return render(request,"lead_update.html",context)

def lead_delete(request,pk):
   lead = Lead.objects.get(id=pk)
   lead.delete()
   return redirect("/leads")