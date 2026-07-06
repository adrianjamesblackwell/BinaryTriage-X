# ADR-001

# Adopt a Central Sample Domain Model

---

## Status

Accepted

---

## Date

2026-07-05

---

## Authors

Blackwell Toolworks Engineering

---

# Problem Statement

BinaryTriage-X consists of multiple independent analysis modules.

Each module extracts different information from the analyzed executable.

Without a shared domain model, every module would return independent dictionaries, lists, or custom structures.

As the platform grows, this approach would lead to:

* duplicated information
* inconsistent interfaces
* increased coupling
* difficult testing
* complicated reporting
* poor long-term maintainability

A unified representation of the binary is required.

---

# Context

BinaryTriage-X follows a staged analysis pipeline.

The pipeline includes:

* Intake
* File Type Detection
* Hashing
* Metadata
* Executable Parsing
* Static Analysis
* IOC Extraction
* Detection
* Threat Intelligence
* Scoring
* Reporting

Every stage contributes additional information.

The architecture therefore requires a shared object that evolves throughout the analysis process.

---

# Engineering Requirements

The selected solution must satisfy the following requirements.

* Single source of truth
* Predictable data flow
* Easy serialization
* Type safety
* Testability
* Extensibility
* Clear ownership
* Compatibility with future plugins
* Compatibility with future APIs
* Compatibility with future distributed analysis

---

# Options Considered

## Option A

Independent dictionaries.

### Advantages

* Very simple implementation
* Minimal initial effort

### Disadvantages

* Poor scalability
* Duplicate data
* Weak typing
* Difficult reporting
* Difficult testing

---

## Option B

Global shared state.

### Advantages

* Easy access

### Disadvantages

* Hidden dependencies
* Difficult debugging
* Poor modularity
* Unsafe future concurrency

---

## Option C

Central Sample Domain Model.

### Advantages

* Explicit ownership
* Structured data
* Easier testing
* Better serialization
* Future extensibility
* Cleaner architecture

### Disadvantages

* Additional model layer
* Slightly higher implementation effort

---

# Decision

BinaryTriage-X adopts a central Sample domain model.

Every analysis stage receives the same Sample instance.

Every module enriches the Sample with new information.

The Sample object represents the complete state of the analysis.

---

# Rationale

The Sample model establishes a single source of truth for the entire platform.

Instead of creating multiple disconnected analysis outputs, all evidence becomes part of one structured object.

This significantly improves:

* readability
* maintainability
* debugging
* testing
* reporting
* future extensibility

The Sample model also aligns with the long-term objective of evolving BinaryTriage-X into a reusable analysis framework rather than a collection of utility scripts.

---

# Trade-offs

The chosen architecture introduces an additional abstraction layer.

Engineers must understand the Sample object before implementing new modules.

However, this small increase in initial complexity substantially reduces long-term maintenance costs.

The trade-off is considered acceptable.

---

# Consequences

## Positive

* Unified analysis object
* Consistent interfaces
* Simplified reporting
* Easier unit testing
* Cleaner architecture
* Better documentation
* Improved extensibility

## Negative

* Slightly higher implementation effort
* Additional documentation
* New contributors must understand the object model

---

# Implementation Impact

The following components are affected.

Current

* models/sample.py
* core/hashing.py
* core/metadata.py

Future

* formats/
* detection/
* intel/
* scoring/
* reporting/

Every future module must update the Sample object instead of creating independent analysis structures.

---

# Verification Strategy

The decision will be validated through:

* Unit tests
* Integration tests
* Serialization tests
* Documentation review
* Code review

The architecture is considered successful if every analysis stage can operate using only the Sample object and its documented interfaces.

---

# Future Evolution

The Sample object currently stores several generic collections.

Future versions should replace these with strongly typed domain models, including:

* Metadata
* Evidence
* Finding
* IOC
* ThreatScore
* Report
* Section
* ImportEntry
* ExportEntry
* Signature
* Capability

This evolution should occur without changing the fundamental architecture established by this ADR.

---

# Related Documents

* 01-system-architecture.md
* 02-system-pipeline.md
* 05-data-model.md

---

# Related ADRs

Future ADRs expected to build upon this decision:

* ADR-002 Linear Analysis Pipeline
* ADR-003 SHA256 Primary Identity
* ADR-004 Strongly Typed Domain Models

---

# Revision History

| Version | Date       | Description     |
| ------- | ---------- | --------------- |
| 1.0     | 2026-07-05 | Initial version |
