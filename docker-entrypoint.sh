#!/bin/bash
set -e

echo "Aguardando o banco de dados iniciar..."

until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  sleep 1
done

echo "Banco de dados pronto. Rodando migrações..."

aerich upgrade

echo "Iniciando servidor..."
exec hypercorn run:app --bind 0.0.0.0:8000 --reload
