from django import forms
from .models import *
from datetime import datetime




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'ordem':forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': ''}),
        }
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome  
    
    def clean_ordem(self):
        ordem = self.cleaned_data.get('ordem')
        if ordem <= 0:
            raise forms.ValidationError("O campo ordem deve ser maior que zero.")
        return ordem

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'datanasc']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf': forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
            'datanasc': forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) < 14:
            raise forms.ValidationError("O CPF deve ter pelo menos 14 caracteres.")
        return cpf

    def clean_datanasc(self):
        datanasc = self.cleaned_data.get('datanasc')
        if datanasc:
            hoje = datetime.today().date()
            if datanasc > hoje:
                raise forms.ValidationError("A data de nascimento não pode ser maior que o dia de hoje.")
            idade = hoje.year - datanasc.year - ((hoje.month, hoje.day) < (datanasc.month, datanasc.day))
            if idade < 18:
                raise forms.ValidationError("O cliente deve ter pelo menos 18 anos.")
        return datanasc     