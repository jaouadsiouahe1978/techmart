# Journal TechMart

## Sprint 1 — Python scripts infra
**Dates :** 11/04 → 15/04/2026
**Tag :** v0.1
**Statut :** ✅ LIVRÉ

### User Stories livrées

| US | Fichier | Fonctionnalité |
|----|---------|---------------|
| US01 | `infra_check.py` | Vérifie CPU (OK/WARN/CRIT), RAM, liste les containers Docker actifs |
| US02 | `services.py` | Vérifie la connectivité de chaque service sur son port (DOWN/OK) |
| US03 | `log_analyzer.py` | Analyse `/var/log/syslog`, comptage erreurs par service, affiche TOP 3 |
| US04 | `alert_checker.py` | Teste les ports, distingue CRITICAL (services vitaux) vs WARNING |

### Ce qui a été fait
- Lecture de `/proc/stat` pour CPU, `/proc/meminfo` pour RAM
- Connexions socket pour vérifier les services (Flask, Postgres, Redis, Nginx)
- Parsing de logs avec dictionnaire + tri par valeur (`sorted + lambda`)
- Gestion de la criticité par flag booléen dans les données

### Rétro Sprint 1
- **What went well :** Scripts fonctionnels, lecture /proc maîtrisée, logique de tri comprise
- **What to improve :** services.py contient plusieurs exercices mélangés — à nettoyer en Sprint 3
- **Dette technique :** Pas de gestion d'exception sur l'ouverture des fichiers /proc

---

## Sprint 2 — Shell scripting
**Dates :** 17/04 → 23/04/2026
**Tag :** v0.2 (prévu)
**Statut :** 🔜 À venir
