# Modern-DE-Pipeline

A personal modern data engineering pipeline built with free and open-source tools.

## Stack

- Redpanda
- MinIO
- Iceberg
- dbt
- Dagster
- k3d

## Installing deps:

```bash
make bootstrap
make setup
```

## Local Redpanda setup

The repo now starts with a small week-1-friendly Redpanda stack:

- 1 Redpanda broker
- 1 Redpanda Console instance
- no SASL yet
- topic auto-creation disabled so you create topics on purpose

Run it from `infra/`:

```bash
docker compose up -d
```

Open Redpanda Console at `http://localhost:8080`.

Create the first topic with:

```bash
docker compose exec redpanda-0 rpk topic create modern-pipeline
```
