def email_valido(email):
    return "@" in email and "." in email

def dividir(a,b):
    if b == 0:
        return None
    return a / b

def email_validado():
    assert email_valido("gucabral447@gmail.com") == True

def validar_dividir():
    assert dividir(4 / 2)  == True