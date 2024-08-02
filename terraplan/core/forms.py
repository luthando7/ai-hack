from django import forms


class CropDataForm(forms.Form):
    temperature = forms.FloatField(label="Temperature (°C)")
    humidity = forms.FloatField(label="Humidity (%)")
    ph_level = forms.FloatField(label="pH Level")
    soil_moisture = forms.FloatField(label="Soil Moisture (%)")
    nitrogen_level = forms.FloatField(label="Nitrogen Level (ppm)")
    phosphorus_level = forms.FloatField(label="Phosphorus Level (ppm)")
    altitude = forms.FloatField(label="Altitude (meters)")