from django.shortcuts import render, redirect
from .forms import UserSignatureForm
from .models import UserSignature

def signature_form(request):
    if request.method == 'POST':
        form = UserSignatureForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form data in session or temporary storage
            request.session['form_data'] = form.cleaned_data
            return redirect('signature_pad')
    else:
        form = UserSignatureForm()
    return render(request, 'signature_form.html', {'form': form})

def signature_pad(request):
    form_data = request.session.get('form_data', {})
    form = UserSignatureForm(initial=form_data)
    return render(request, 'signature_pad.html', {'form': form})

def submit_form(request):
    if request.method == 'POST':
        form = UserSignatureForm(request.POST, request.FILES)
        if form.is_valid():
            user_signature = form.save()  # Save form data and file
            if 'form_data' in request.session:
                del request.session['form_data']
            return redirect('success')
    return redirect('signature_form')

def success(request):
    signatures = UserSignature.objects.all()
    return render(request, 'success.html', {'signatures': signatures})
