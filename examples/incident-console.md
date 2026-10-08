# Worked create example: incident triage console

This is a synthetic product brief and illustrative result, not user research or a production implementation.

## Brief

An on-call operator needs to find unowned urgent incidents, claim one, and open its context. The intended environment is a desktop browser with keyboard support. The local prototype has synthetic incident records; it cannot page staff or change a production incident service.

## Concrete direction

Use a ranked incident table as the working area, with urgency, service, incident title, age, and owner in consistent columns. Place current scope/filter and data mode above it. A detail panel shows evidence, recent events, and the selected incident's action. Avoid unrelated business KPIs.

| Urgency | Service | Incident | Age | Owner |
| --- | --- | --- | --- | --- |
| Critical | Checkout | Payment retries increasing | 7 min | Unassigned |
| High | Identity | Sign-in failures above threshold | 14 min | Assigned |
| Medium | Search | Delayed indexing | 31 min | Unassigned |

Rows are original synthetic content. “Critical” is a fixture label, not a measured business severity.

A primary “Claim incident in this demo” action changes local prototype state and states what is saved. If prototype state is session-only, say so; do not show “Synced to incident service.” Detail and ownership changes remain associated with the selected incident ID.

## Relevant state specification

- Loading: show that records are being retrieved; preserve layout.
- Empty: no incidents match; show the current filters and a way to reset.
- Error: record retrieval failed; keep the previous result visibly stale when useful and offer retry.
- Claim success: the actual local owner updates.
- Claim failure in production: permission/concurrency failure preserves context and explains recovery.
- Keyboard: rows and actions have an understandable focus path and names.
- Narrow view: prioritize incident identification and urgency; retain reachable owner/detail information instead of shrinking every column.

## Why this is a valid exception

High density supports triage/comparison here. It needs actual readability/target/reflow checks; it is not justified by “expert users” alone. A focused intake form or heterogeneous browse collection would need a different structure.

## What remains unproven

Priority rules, representative device constraints, user terminology, and actual completion efficiency need product/user evidence. This example specifies a design; a real “build” request must also deliver and verify the requested implementation.
