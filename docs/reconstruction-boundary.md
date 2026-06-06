# Reconstruction Boundary

## What This Public Repo Keeps

- orchestration over multiple workflow modules
- a backend refresh pass that produces structured dashboard data
- a lightweight internal tooling dashboard
- representative reporting and transformation workflows
- the adapter-layer idea for browser and HTTP integrations

## What It Intentionally Drops

- raw credentials and token helpers
- vendor-specific selectors and endpoints
- private recipients or outbound notification transports
- cached historical operational data
- customer names, addresses, phone numbers, and email addresses
- brittle machine-local paths and deployment glue

## Historical Sources Behind This Reconstruction

Primary source branch:

- `E:\7k data\Latest 7Kauto\CurrentlyDeployed`

Lineage-only support:

- `E:\7k data\Latest 7Kauto\CurrentlyDeployedLEGACY`
- `E:\7k data\Latest 7Kauto\V3`
- `E:\7k data\Latest 7Kauto\V2`

## Why The Demo Uses Fixtures

The historical system was useful because it connected many private systems at once. Publishing that system raw would mean publishing:

- confidential access patterns
- operational naming
- sensitive records
- environment-specific assumptions

Fixtures keep the architecture visible while removing the parts that should never leave the archive.

## Honest Limits

This repo is not a full export of the historical private runtime. It is a shaped reconstruction meant to show:

- how tasks were orchestrated
- how collector outputs fed a dashboard
- how automation evolved from script fragments into a system

That is the correct public boundary for the first release.
