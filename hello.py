#!/usr/bin/env python3
import os

current_lang = os.getenv("LANG", "en_US")[:5]
msg = ("Hello World")

if current_lang == "pt_BR":
    msg = ("Olá Mundo")
elif current_lang == "es_ES":
    msg = ("Hola Mundo")
elif current_lang == "fr_FR":
    msg = ("Bonjour le monde")    

print(msg) 
