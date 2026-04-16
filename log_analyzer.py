erreurs = {}

with open("/var/log/syslog") as f:
    for ligne in f:
        if "error" in ligne.lower():
            service = ligne.split()[2]
            if service in erreurs:
                erreurs[service] += 1
            else:
                erreurs[service] = 1

print(erreurs)


tri = sorted(erreurs.items(), key=lambda x: x[1], reverse=True)

print("\n=== TOP 3 erreurs ===")
for i, (service, nb) in enumerate(tri[:3]):
    print(f"[{i+1}] {service} : {nb} fois")