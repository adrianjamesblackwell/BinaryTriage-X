# Data Model

## Purpose

This document defines the core data model of BinaryTriage-X.

The platform is designed around structured domain objects rather than loosely organized dictionaries.

Every analysis stage enriches a shared object model that represents the current binary under investigation.

This approach improves:

* readability
* maintainability
* type safety
* testing
* future extensibility

---

# Modeling Philosophy

BinaryTriage-X models the analysis itself.

It does not simply process files.

Every binary becomes a structured analysis object.

The platform therefore revolves around domain models rather than individual functions.

---

# Core Entity

## Sample

The Sample object represents one binary under analysis.

Every pipeline stage enriches this object.

The Sample object is never replaced.

It accumulates information until the final report is produced.

---

# Sample Lifecycle

```text
Input File

↓

Validated File

↓

Executable Type

↓

Hashes

↓

Metadata

↓

Executable Structure

↓

Evidence

↓

Findings

↓

Threat Context

↓

Scores

↓

Reports
```

---

# Domain Models

## Sample

Purpose

Represents one executable under investigation.

Contains

* identity
* metadata
* evidence
* findings
* scores
* reports

Lifecycle

Entire pipeline.

---

## Metadata

Purpose

Represents descriptive information.

Contains

* filename
* extension
* size
* timestamps
* executable type
* hashes

Producer

Metadata Engine

Consumers

Reporting

Scoring

Dashboard

---

## Evidence

Purpose

Represents raw observable information.

Examples

* Import table entries
* Export table entries
* Strings
* Sections
* Entropy
* Resources
* Digital signatures

Evidence never contains conclusions.

Evidence represents observations.

---

## Finding

Purpose

Represents an explainable analytical conclusion.

Every Finding references one or more Evidence objects.

Examples

Packed executable

Suspicious imports

High entropy section

Embedded PowerShell

Each Finding contains:

* title
* description
* severity
* confidence
* evidence references

---

## IOC

Purpose

Represents Indicators of Compromise.

Examples

* URLs
* Domains
* IP addresses
* Registry paths
* Email addresses
* Mutex names
* File paths

Producer

IOC Extraction Engine

Consumers

Threat Intelligence

Reporting

External integrations

---

## Threat Context

Purpose

Represents contextual intelligence.

Contains

* MITRE ATT&CK mappings
* Categories
* Related behaviors
* Threat notes

Threat Context never changes Evidence.

It only enriches interpretation.

---

## Threat Score

Purpose

Represent investigation priority.

Contains

* score
* confidence
* priority
* explanation

The score is never generated without Findings.

---

## Report

Purpose

Represent final analysis output.

Formats

JSON

HTML

Case Bundle

Reports should never calculate new information.

Reports only present existing data.

---

# Relationships

```text
Sample

├── Metadata

├── Evidence

│      │

│      ├── Strings

│      ├── Imports

│      ├── Sections

│      ├── Resources

│      └── Entropy

│

├── Findings

│

├── IOC

│

├── Threat Context

│

├── Threat Score

│

└── Reports
```

---

# Data Ownership

Every model has exactly one owner.

Example

Metadata Engine

↓

owns Metadata

Detection Engine

↓

owns Findings

IOC Engine

↓

owns IOC

Scoring Engine

↓

owns Threat Score

Reporting Engine

↓

owns Reports

No module should modify another module's internal data.

---

# Immutability Rules

Evidence should be treated as immutable after creation.

Findings should reference Evidence instead of copying it.

Reports should never modify Sample contents.

Scoring should never alter Findings.

This prevents accidental data corruption.

---

# Serialization

Every domain model should support structured serialization.

Primary serialization target:

JSON

Future serialization targets:

* YAML
* MessagePack
* Protocol Buffers

---

# Future Domain Models

Future versions may introduce:

* Section
* Import
* Export
* Resource
* Certificate
* Signature
* Packer
* StringArtifact
* Capability
* RuleMatch
* SandboxResult
* TimelineEvent

These models should integrate with the existing object hierarchy rather than introducing parallel structures.

---

# Design Principles

BinaryTriage-X follows several modeling principles.

* Domain-driven organization
* Strong typing
* Single ownership
* Immutable evidence
* Explainable findings
* Serializable models
* Explicit relationships

The objective is to model binary analysis as an engineering domain rather than as a collection of utility functions.

---

# Summary

The data model is the foundation of BinaryTriage-X.

Every module contributes information to structured domain objects.

Every object has a clear responsibility.

Every relationship is explicit.

This architecture enables the platform to grow without sacrificing readability or maintainability.
