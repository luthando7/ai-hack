from django.shortcuts import render
from .forms import CropDataForm
from nn.train import evaluate


def home(request):
    return render(request, template_name='core/index.html')


def crop_data(request):
    if request.method == 'POST':
        form = CropDataForm(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data['temperature']
            humidity = form.cleaned_data['humidity']
            ph_level = form.cleaned_data['ph_level']
            soil_moisture = form.cleaned_data['soil_moisture']
            nitrogen_level = form.cleaned_data['nitrogen_level']
            phosphorus_level = form.cleaned_data['phosphorus_level']
            altitude = form.cleaned_data['altitude']

            data = evaluate([temperature, humidity, ph_level, soil_moisture, nitrogen_level, phosphorus_level, altitude])
            crop = ''
            if data == 0:
                crop = 'Corn'
            elif data == 1:
                crop = 'Soybean'
            elif data == 2:
                crop = 'Wheat'

            context = {'data': crop}

            return render(request, 'core/crop_data.html', context)
    else:
        form = CropDataForm()

    return render(request, 'core/crop_data.html', {'form': form})
