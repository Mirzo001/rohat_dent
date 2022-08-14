from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class UserChangeView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/change.html'
    
