from pathlib import Path
import json

carpeta = Path("datos") / "json"
carpeta.mkdir(parents=True, exist_ok=True)

archivo = carpeta / "datos.json"

datos = [
    {"nombre": "Roel", "edad": 30},
    {"nombre": "Ana", "edad": 25},
]

with open(archivo, mode = "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)

with open(archivo, mode = "r", encoding="utf-8") as f:
    datos = json.load(f)

print(datos)