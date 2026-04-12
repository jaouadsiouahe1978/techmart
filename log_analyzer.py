compteur = 0

with open("/var/log/syslog") as f:
    for ligne in f:
        if "error" in ligne or "ERROR" in ligne:
            compteur+= 1

print(f"Erreurs trouvées : {compteur}")