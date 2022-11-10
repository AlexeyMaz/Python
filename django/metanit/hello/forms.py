from django import forms


class TableChoice(forms.Form):
    tables = forms.ChoiceField(choices=((1, ""), (2, "Caroges"), (3, "Customers"),
                                        (4, "CustomersCargoes"), (5, "Dispatchers"), (6, "Drivers")))


class Authorization(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")


class Registration(forms.Form):  # фамилия, имя, отчество, e-mail, пароль
    last_name = forms.CharField(label="Фамилия")
    first_name = forms.CharField(label="Имя")
    patronymic = forms.CharField(label="Отчество")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
