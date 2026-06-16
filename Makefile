.PHONY: bootstrap setup

bootstrap:
	@echo "Installing rpk cli (Redpanda CLI)..."
	brew install redpanda-data/tap/redpanda

setup:
	@echo "UV sync setup..."
	uv sync
