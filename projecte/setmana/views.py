from django.shortcuts import redirect
from django.http import HttpResponse

def home(request): # pàgina principal
    html = """<h1>Dies de la setmana</h1>
    <h3>Per seleccionar un dia de la setmana, afegeix al final de la URL el número corresponent:</h3>
    <h4>si poses un numero que no estigui entre 1 i 7 et redirigira a la pàgina principal</h4>""" 
    return HttpResponse(html)


def num(request, num: str): # pàgina que mostra el dia de la setmana segons el número introduït
    try:
        num = int(num) # pasa de string a enter
    except ValueError:
        return redirect('home')  
    
    dies_setmana = { # diccionari dels dies de la setmana
        1: "Dilluns",
        2: "Dimarts",
        3: "Dimecres",
        4: "Dijous",
        5: "Divendres",
        6: "Dissabte",
        7: "Diumenge"
    }
    img = {
        1: "Dilluns.jpg",
        2: "dimarts.jpg",
        3: "dimecres.jpg",
        4: "dijous.jpg",
        5: "divendres.jpg",
        6: "dissabte.jpg",
        7: "diumenge.jpg"
    }

    if num not in dies_setmana: # si no esta a dintre dels dies de la setmana del diccionari t'envia a home 
        return redirect('home')

    dia = dies_setmana[num] # agafa el dia corresponent al número
    img_dia = img.get(num)  # agafa la imatge corresponent al dia

    
    return HttpResponse( # mostra el dia i la imatge
            f'<h1>El {num} és {dia}</h1>' # mostra el dia
            f'<img src="/img/{img_dia}" alt="{dia}">' # mostra la imatge
        )
