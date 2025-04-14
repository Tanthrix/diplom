from django import forms
from .models import CustomUser, Device, Specification, Room, Role

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'password1', 'password2', 'roles']
        labels = {
            'username': 'Логин',
            'full_name': 'Полное имя',
            'roles': 'Роли',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserEditForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'roles']
        labels = {
            'username': 'Логин',
            'full_name': 'Полное имя',
            'roles': 'Роли',
        }

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'serial_number', 'status', 'room', 'photo']
        labels = {
            'name': 'Название устройства',
            'serial_number': 'Серийный номер',
            'status': 'Статус',
            'room': 'Комната',
            'photo': 'Фотография',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['name', 'value']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        value = cleaned_data.get('value')
        if not name or not value:
            raise forms.ValidationError('Имя и значение характеристики не могут быть пустыми.')
        return cleaned_data

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']
        widgets = {
            'role_name': forms.Select(attrs={'class': 'form-control'}),
        }