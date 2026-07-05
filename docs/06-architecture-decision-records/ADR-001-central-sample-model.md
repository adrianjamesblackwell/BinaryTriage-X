# ADR-001

## Title

Adopt a Central Sample Object

---

## Status

Accepted

---

## Context

BinaryTriage-X consists of multiple independent analysis modules.

Without a shared domain object, each module would produce isolated dictionaries and unrelated data structures.

This would increase coupling, duplicate information, and complicate reporting.

---

## Options Considered

### Option A

Independent dictionaries.

### Option B

Global state.

### Option C

Central Sample domain object.

---

## Decision

BinaryTriage-X adopts a central Sample object.

Every analysis stage receives the same Sample instance.

Every stage enriches the Sample with additional evidence.

---

## Rationale

The Sample model provides:

* predictable data flow
* reduced duplication
* easier testing
* better maintainability
* simplified reporting

It also prepares the platform for future plugin support and distributed analysis.

---

## Consequences

Positive

* unified architecture
* explicit data ownership
* simpler serialization

Negative

* additional model layer
* initial implementation effort

---

## Future Considerations

The Sample object may eventually contain strongly typed child models instead of generic dictionaries.
