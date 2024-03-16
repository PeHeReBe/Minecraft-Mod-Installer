import requests
import sys

#from tqdm import tqdm

url = 'https://codeload.github.com/Rojoad/Zombie/zip/refs/heads/main?token=AM6QEWBSDHI7RZPLKT52LXLF6XM4Q'  # Die URL der Datei, die du herunterladen möchtest
ziel_datei = 'mcp.zip'  # Der Name der heruntergeladenen Datei


print("Hallo, Welt!")


while True:
    antwort = input("Möchtest du fortfahren? (Ja/Nein): ").strip().lower()
    
    if antwort == "ja":
        print("Du hast Ja gewählt. Das Programm wird fortgesetzt.")
        break
    elif antwort == "nein":
        print("Du hast Nein gewählt. Das Programm wird beendet.")
        sys.exit()
        break
    else:
        print("Ungültige Eingabe. Bitte antworte mit 'Ja' oder 'Nein'.")

# Die Datei herunterladen
response = requests.get(url, stream=True)

# Überprüfen, ob der Download erfolgreich war
if response.status_code == 200:
    # Die Größe der Datei abrufen
    gesamtgroesse = int(response.headers.get('content-length', 0))


    # Ein Fortschrittsbalken mit tqdm initialisieren
    with open(ziel_datei, 'wb') as file, tqdm(
            desc=ziel_datei,
            total=gesamtgroesse,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for datenblock in response.iter_content(1024):
            file.write(datenblock)
            bar.update(len(datenblock))

    print("Die Datei wurde erfolgreich heruntergeladen.")
else:
    print("Fehler beim Herunterladen der Datei:", response.status_code)