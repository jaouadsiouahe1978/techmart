 # TechMart — Infrastructure prod-ready

  ## Scénario
  Startup e-commerce. Infra sur un seul serveur, déploiement manuel, aucun monitoring.
  Mission : moderniser de A à Z.

  ## Stack
  - App : Python Flask
  - BDD : PostgreSQL
  - Cache : Redis
  - Proxy : Nginx
  - CI/CD : GitLab
  - Conteneurs : Docker + Compose
  - Orchestration : K3s
  - Monitoring : Prometheus + Grafana
  - IaC : Ansible + Terraform

  ## Structure
  techmart/
  ├── scripts/
  ├── docs/
  ├── docker/
  ├── kubernetes/
  ├── ansible/
  ├── terraform/
  └── monitoring/
