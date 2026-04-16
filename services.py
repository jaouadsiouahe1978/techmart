services = ["nginx", "prometheus", "grafana", "postgres", "alertmanager"]


print(services[0])
print(services[-1])
print(len(services))
services.append("traefik")

résultat = [i for i in services if "a" in i]
print(résultat)
print(services)


###################hosts##############

hosts = ["192.168.1.150", "192.168.1.164", "192.168.1.80", "10.0.0.2", "172.1.2.45"]

hosts.append("10.0.0.6")

print(hosts[2])
hosts.pop(-1)
hosts.sort()
print(hosts)
if "10.0.0.1" in hosts:
    print("True")
else:
    print("False")

#########################ports###############
port = [22, 80, 443, 3306, 5432, 9090]


print(port[2:])
port.reverse()


##############################################ports##############
ports = [80, 443, 9090, 3000]

result = [p for p in ports if p > 1000]
print(result)


#############################################services5.py###################
 
  ############TP — services.py#####

 # Contexte : Tu reçois une liste de services avec leur statut. Tu dois la traiter.

  #services = [
   #   {"name": "nginx",        "status": "active",   "port": 80},
   #   {"name": "prometheus",   "status": "inactive", "port": 9090},
    #  {"name": "grafana",      "status": "active",   "port": 3000},
     # {"name": "alertmanager", "status": "inactive", "port": 9093},
      #{"name": "postgres",     "status": "active",   "port": 5432},
      #{"name": "traefik",      "status": "active",   "port": 8080},
  #]

 # Objectifs :

  #1. Créer une liste actifs — uniquement les services avec status == "active"
  #2. Créer une liste inactifs — uniquement les services inactive
  #3. Afficher les actifs triés par nom (ordre alphabétique)
  #4. Afficher un résumé : "3 actifs / 2 inactifs"

  #Contraintes :
  #- Utiliser des list comprehensions pour filtrer
  #- Utiliser sorted() pour le tri
  #- Pas d'import, pas de fonctions — code direct

  #"Crée le fichier ~/services.py et montre-moi le code quand c'est prêt.


services = [
     {"name": "nginx",        "status": "active",   "port": 80},
     {"name": "prometheus",   "status": "inactive", "port": 9090},
     {"name": "grafana",      "status": "active",   "port": 3000},
     {"name": "alertmanager", "status": "inactive", "port": 9093},
     {"name": "postgres",     "status": "active",   "port": 5432},
     {"name": "traefik",      "status": "active",   "port": 8080},
 ]

actifs = [a for a in services if a["status"] == "active"]


inactifs = [b for b in services if b["status"] == "inactive"]


actif_trie = sorted(actifs, key=lambda x: x["name"])

print(actif_trie)




print(f"{len(actifs)} actifs /  {len(inactifs)} inactifs")

################################service_monitor.py ####################################


import socket

services = [
     {"name": "flask",  "port" : 5000},
     {"name": "postgres",   "port" : 5432},
     {"name": "redis",	"port" : 6379},
     {"name": "nginx",	 "port" : 80},
]



for service in services:
    s = socket.socket()
    try:
        s.connect(("localhost", service["port"]))
        print(f"service {service['name']} : OK")
    except:
        print(f"service {service['name']} : DOWN")

#################################alert_checker.py########################################
import socket
services = [
      {"name": "flask",    "port": 5000, "critical": True},
      {"name": "postgres", "port": 5432, "critical": True},
      {"name": "redis",    "port": 6379, "critical": False},
      {"name": "nginx",    "port": 80,   "critical": False},
]

for service in services:
    s = socket.socket()
    try:
        s.connect(("localhost", service["port"]))
        print(f"service {service['name']} : OK")
    except:
        if service["critical"] == True:
            print(f"service {service['name']} : CRITICAL")
        else:
            print(f"service {service['name']} : WARNING")

