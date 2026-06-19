#!/usr/bin/env sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "Uso: sh scripts/deploy.sh <env-file> <compose-file>"
  exit 1
fi

ENV_FILE="$1"
COMPOSE_FILE="$2"

if [ ! -f "$ENV_FILE" ]; then
  echo "Falta el archivo $ENV_FILE"
  exit 1
fi

docker compose \
  --env-file "$ENV_FILE" \
  -f "$COMPOSE_FILE" \
  up -d --force-recreate --remove-orphans
