STORY = {
    "baslangic": {
        "metin": "Karanlik bir ormanda uyaniyorsun. Onunde iki patika var.",
        "secenekler": [
            ("Sol patikaya git", "sol"),
            ("Sag patikaya git", "sag"),
        ],
    },
    "sol": {
        "metin": "Bir nehre ulastin. Su berrak ve soguk.",
        "secenekler": [
            ("Sudan ic", "son_iyi"),
            ("Geri don", "baslangic"),
        ],
    },
    "sag": {
        "metin": "Eski bir kulube gordun. Kapi aralik.",
        "secenekler": [
            ("Iceri gir", "son_kotu"),
            ("Geri don", "baslangic"),
        ],
    },
    "son_iyi": {
        "metin": "Tazelendin ve yolunu buldun. SON.",
        "secenekler": [("Bastan basla", "baslangic")],
    },
    "son_kotu": {
        "metin": "Kulube tuzakti! Kayboldun. SON.",
        "secenekler": [("Bastan basla", "baslangic")],
    },
}
