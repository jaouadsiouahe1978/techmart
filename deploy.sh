#!/bin/bash
if [ "$(systemctl is-active docker)" != "active" ]; then
	echo "Docker n'est pas actif"
	exit 1
fi
echo "Docker est actif"
docker pull techmart-app:latest

if [ "$(docker inspect -f '{{.State.Running}}' techmart-app 2>/dev/null)" == "true" ]; then

	echo "Arrêt du conteneur techmart-app"
	docker stop techmart-app
fi
docker run -d -p 5000:5000 --name techmart-app --restart=unless-stopped techmart-app:latest
sleep 3
if [ "$(docker inspect -f '{{.State.Running}}' techmart-app 2>/dev/null)" == "true" ]; then
        echo "Déploiement réussi — techmart-app tourne"
else
        echo "ERREUR — le conteneur n'a pas démarré"
        exit 1
fi
exit 0
