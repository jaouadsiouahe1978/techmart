import os
text = os.popen ("docker ps --format '{{.Names}}'").read()

liste_docker = [x for x in text.split("\n") if x != ""]

liste_docker.sort()

print(liste_docker)

with open("/proc/stat") as f:
    for ligne in f:
        colonnes = ligne.split()
        if colonnes[0] == "cpu":
            idle  = int(colonnes[4])
            total = int(colonnes[1]) + int(colonnes[2]) + int(colonnes[3]) + int(colonnes[4]) + int(colonnes[5])
            cpu_usage = round(100 - (idle / total * 100))
            break

if cpu_usage >= 90:
    print(f"CPU : CRIT ({cpu_usage}%)")
elif cpu_usage >= 70:
    print(f"CPU : WARN ({cpu_usage}%)")
else:
    print(f"CPU : OK ({cpu_usage}%)")

with open("/proc/meminfo") as f:
      for ligne in f:
          if "MemTotal" in ligne:
              ram_total = int(ligne.split()[1])
          if "MemAvailable" in ligne:
              ram_dispo = int(ligne.split()[1])

ram_usage = round(100 - (ram_dispo / ram_total * 100))
