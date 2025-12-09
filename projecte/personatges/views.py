from django.shortcuts import render

# Diccionari amb tots els personatges i la seva informació
personatges = {
    "Eren": {
        "nom": "Eren Jaeger",
        "frase": "¡No soy un héroe! ¡Quiero ser libre!",
        "img": "/img/AOT/eren.jpg",
        "opcio": "eren",
    },
    "Mikasa": {
        "nom": "Mikasa Ackerman",
        "frase": "Protegeré a Eren cueste lo que cueste.",
        "img": "/img/AOT/mikasa.jpg",
        "opcio": "mikasa",
    },
    "Armin": {
        "nom": "Armin Arlert",
        "frase": "La verdadera fuerza está en la mente y la estrategia.",
        "img": "/img/AOT/armin.jpg",
        "opcio": "armin",
    },
    "Levi": {
        "nom": "Levi Ackerman",
        "frase": "La humanidad solo puede sobrevivir luchando.",
        "img": "/img/AOT/levi.png",
        "opcio": "levi",
    },
    "Historia": {
        "nom": "Historia Reiss",
        "frase": "Haré lo correcto, aunque cueste mi vida.",
        "img": "/img/AOT/historia.jpg",
        "opcio": "historia",
    },
}

from django.shortcuts import render

def home(request):
    # Renderitzem la pàgina principal amb la llista de personatges
    return render(request, "home.html", {
        "mode": "home",
        "personatges": personatges.values(),  # enviem tots els personatges
    })

def personatge(request, opcio):
    # Si l'opció és "home", tornem al menú principal
    if opcio == "home":
        return home(request)

    personatge_trobat = None

    # Busquem quin personatge coincideix amb l'opció
    for p in personatges.values():
        if p["opcio"] == opcio:
            personatge_trobat = p
            break

    # Si existeix, mostrem la seva bio
    if personatge_trobat:
        return render(request, "home.html", {
            "mode": "bio",
            "personatge": personatge_trobat,
        })

    # Si no existeix, mostrem un error
    return render(request, "home.html", {
        "mode": "error",
        "meme_url": "/img/AOT/error.jpg",
        "missatge_error": "Aquest personatge no existeix.",
    })
