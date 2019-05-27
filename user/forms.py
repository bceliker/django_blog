from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Password", widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=10, label = "Password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10,label="Parola doğrula",widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm:
            if password!=confirm:
                raise forms.ValidationError("Parolalar uyuşmuyor...")
            else:
                pass
        else:
            raise forms.ValidationError("Parola alanları girilmeli...")
       
        values = {
            "username":username,
            "password":password
        } 
        return values

