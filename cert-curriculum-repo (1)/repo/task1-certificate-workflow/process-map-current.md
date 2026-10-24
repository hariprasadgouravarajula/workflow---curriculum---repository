# Current-state process map (SYNTHETIC / ILLUSTRATIVE, replace with your observed map)

```mermaid
flowchart TD
  A[Student fills paper form at counter] --> B[Clerk checks form and documents]
  B -->|incomplete| X1[Student sent back; no tracking] --> A
  B -->|complete| C[Clerk checks dues/eligibility in registers]
  C --> D[File placed in authority's tray]
  D -->|authority absent| X2[File waits; student asks by phone] --> D
  D --> E[Authority signs]
  E --> F[Clerk prints, stamps seal]
  F --> G[Student collects at counter]
```

| Step | Who (role) | Handoff medium | Approval point | Exceptions |
|---|---|---|---|---|
| Submit | Student | Paper | none | missing purpose or documents |
| Check | Clerk | Paper | clerk completeness check | duplicate/repeat request not noticed |
| Eligibility | Clerk | Register | rule check | dues pending |
| Sign | Authority | Tray | **signature** | authority absent, delay |
| Issue | Clerk | Counter | seal | lost file |
| Collect | Student | Counter | ID check | someone else collecting |
