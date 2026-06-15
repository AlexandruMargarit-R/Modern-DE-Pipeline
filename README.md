# Modern-DE-Pipeline

A personal modern data engineering pipeline built with free and open-source tools.

## Stack

- Redpanda
- MinIO
- Iceberg
- dbt
- Dagster
- k3d

## Local Redpanda setup

The repo now starts with a small week-1-friendly Redpanda stack:

- 1 Redpanda broker
- 1 Redpanda Console instance
- no SASL yet
- topic auto-creation disabled so you create topics on purpose

Run it from `infra/redpanda/docker-compose`:

```bash
docker compose up -d
```

Open Redpanda Console at `http://localhost:8080`.

If one of the default host ports is already taken, override it when you start the stack:

```bash
REDPANDA_KAFKA_PORT=29092 REDPANDA_ADMIN_PORT=29644 REDPANDA_CONSOLE_PORT=8081 docker compose up -d
```

Create the first topic with:

```bash
docker compose exec redpanda rpk topic create raw-events
```

If you want to use `rpk` from your machine, the starter profile is in:

```text
infra/redpanda/docker-compose/rpk-profile.yaml
```
