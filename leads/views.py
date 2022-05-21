
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from leads.forms.forms import LeadForm,LeadModelForm
from leads.models import Lead,Agent
from django.views.generic import DeleteView,UpdateView,ListView,DetailView,CreateView


#class based views
class LeadListView(ListView):
   template_name= 'lead_list.html'
   queryset= Lead.objects.all()
   context_object_name= 'lead'

class LeadDetailView(DetailView):
   template_name = 'lead_detail.html'
   queryset = Lead.objects.all()
   context_object_name = 'lead'

class LeadCreateView(CreateView):
   template_name = 'lead_create.html'
   form_class = LeadModelForm
   
   def get_success_url(self) -> str:
       return reverse("leads:lead-list")

class LeadUpdateView(UpdateView):
   template_name = 'lead_update.html'
   form_class = LeadModelForm
   
   def get_success_url(self) -> str:
       return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
   template_name = 'lead_delete.html'
   form_class = LeadModelForm
   
   def get_success_url(self) -> str:
       return reverse("leads:lead-list")

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