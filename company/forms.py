from django import forms

class subscribe(forms.Form):
    Email=forms.EmailField()
    def __str__(self):
        return self.Email