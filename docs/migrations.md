```bash
# Test
#
# Certificar-se que em run.py: app = create_app("config.TestConfig")
flask db init --directory=migrations/test-migrations
flask db migrate -m "Initial Migration for Test" --directory=migrations/test-migrations
flask db upgrade --directory=migrations/test-migrations 
# Nova migração
flask db stamp head --directory=migrations/test-migrations # Marcar a migração como feita para evitar erros e sincronizar com as tabelas existentes. É recomendado antes de aplicar novas migrações
flask db migrate -m "New Migration for Test" --directory=migrations/test-migrations
flask db upgrade --directory=migrations/test-migrations
#...

# Repetir etapas semelhantes para o ambiente de staging

# Staging
#
# Certificar-se que em run.py: app = create_app("config.StagingConfig")
flask db init --directory=migrations/staging-migrations
flask db migrate -m "Initial Migration for Staging" --directory=migrations/staging-migrations
flask db upgrade --directory=migrations/staging-migrations
#...

# Repetir etapas semelhantes para o ambiente de produção

# Prod
#
# Certificar-se que em run.py:: app = create_app("config.ProdConfig")
flask db init --directory=migrations/prod-migrations
flask db migrate -m "Initial Migration for Prod" --directory=migrations/prod-migrations
flask db upgrade --directory=migrations/prod-migrations
#... 
```