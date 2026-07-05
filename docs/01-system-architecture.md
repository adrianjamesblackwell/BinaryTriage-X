# System Architecture

## Purpose

This document defines the high-level architecture of BinaryTriage-X.

Its purpose is to describe how the system is organized, how information flows through the platform, and how individual modules collaborate to produce an explainable binary triage result.

This document intentionally focuses on architecture rather than implementation details.

---

# Architectural Vision

BinaryTriage-X is designed as a modular analysis platform rather than a monolithic application.

Every component has one clearly defined responsibility.

Each module receives structured input, performs one task, enriches the central analysis object, and forwards it to the next stage.

The architecture emphasizes:

* Modularity
* Explainability
* Reproducibility
* Testability
* Long-term maintainability
* Clear separation of responsibilities

The system is intentionally designed so that future capabilities can be added without redesigning the core architecture.

---

# Core Architectural Principles

## 1. Single Responsibility Principle

Every module performs one logical task.

Examples:

* Intake validates input.
* File Type Detection identifies executable formats.
* Hash Engine generates cryptographic identities.
* Metadata Engine extracts identity information.
* IOC Extraction identifies indicators.
* Reporting generates analyst-friendly outputs.

A module should never perform unrelated work.

---

## 2. Pipeline Architecture

BinaryTriage-X follows a staged processing pipeline.

Each stage receives structured input from the previous stage.

Each stage enriches the central analysis object.

Each stage forwards the updated object to the next stage.

No stage repeats work already performed by another stage.

---

## 3. Sample-Centric Design

The Sample object represents the binary currently under analysis.

Every module operates on the same Sample instance.

The Sample object accumulates evidence throughout the pipeline.

This approach ensures:

* Consistent state management
* Easier debugging
* Predictable data flow
* Simpler reporting
* Reduced duplication

---

## 4. Explainable Analysis

BinaryTriage-X does not produce unsupported conclusions.

Every score must be traceable.

Every finding must include supporting evidence.

Every recommendation must be explainable.

The system assists analysts rather than replacing analyst judgment.

---

## 5. Security by Design

The platform follows defensive engineering principles.

Unknown binaries are never trusted.

Input validation is mandatory.

Analysis is performed in read-only mode.

The platform does not execute unknown binaries during static analysis.

---

# System Layers

## Layer 1 — Command Interface

Purpose:

Provide the user entry point into the platform.

Responsibilities:

* Parse command-line arguments
* Validate user input
* Initialize the analysis pipeline
* Display execution status
* Return structured output

Primary Module:

```text
binarytriage/cli.py
```

---

## Layer 2 — Input Validation

Purpose:

Ensure that the provided input is safe to analyze.

Responsibilities:

* File existence validation
* File accessibility
* File size validation
* Input normalization
* Error reporting

Primary Module:

```text
binarytriage/core/intake.py
```

Output:

Validated file path.

---

## Layer 3 — File Identification

Purpose:

Determine the true executable format.

Responsibilities:

* Read magic bytes
* Detect executable format
* Reject unsupported formats

Supported Formats:

* PE
* ELF
* Mach-O

Primary Module:

```text
binarytriage/core/filetype.py
```

Output:

Executable type.

---

## Layer 4 — Identity Generation

Purpose:

Generate cryptographic identities for the sample.

Responsibilities:

* MD5
* SHA1
* SHA256

Primary Module:

```text
binarytriage/core/hashing.py
```

Output:

Cryptographic hashes.

---

## Layer 5 — Sample Model

Purpose:

Provide the central analysis object shared by the entire pipeline.

Responsibilities:

* Store analysis state
* Store evidence
* Store findings
* Store scores
* Store metadata

Primary Module:

```text
binarytriage/models/sample.py
```

Output:

Enriched Sample object.

---

## Layer 6 — Metadata Extraction

Purpose:

Extract descriptive information about the sample.

Responsibilities:

* Filename
* Extension
* File size
* Timestamps
* Executable type
* Hashes

Primary Module:

```text
binarytriage/core/metadata.py
```

Output:

Sample identity information.

---

## Layer 7 — Format Analysis

Purpose:

Parse executable-specific structures.

Responsibilities:

* PE parsing
* ELF parsing
* Mach-O parsing

Primary Modules:

```text
binarytriage/formats/pe.py
binarytriage/formats/elf.py
binarytriage/formats/macho.py
```

Output:

Executable structure.

---

## Layer 8 — Static Analysis

Purpose:

Extract observable static characteristics.

Responsibilities:

* Strings
* Entropy
* Sections
* Imports
* Exports
* Symbols

Output:

Static analysis artifacts.

---

## Layer 9 — Detection

Purpose:

Identify suspicious characteristics.

Responsibilities:

* Suspicious indicators
* Packer detection
* YARA matching
* Sigma mapping
* Blackwell signatures

Primary Modules:

```text
binarytriage/detection/
```

Output:

Structured findings.

---

## Layer 10 — Threat Intelligence

Purpose:

Provide operational context.

Responsibilities:

* IOC extraction
* MITRE ATT&CK mapping
* Threat context

Primary Modules:

```text
binarytriage/intel/
```

Output:

Threat intelligence context.

---

## Layer 11 — Threat Scoring

Purpose:

Prioritize analyst attention.

Responsibilities:

* Threat score
* Confidence score
* Investigation priority

Primary Modules:

```text
binarytriage/scoring/
```

Output:

Structured scoring information.

---

## Layer 12 — Reporting

Purpose:

Present analysis results.

Responsibilities:

* JSON reports
* HTML dashboard
* Analyst summary
* Case bundle generation

Primary Modules:

```text
binarytriage/reporting/
```

Output:

Human-readable and machine-readable reports.

---

# Complete Analysis Pipeline

```text
User
 │
 ▼
CLI
 │
 ▼
Input Validation
 │
 ▼
File Type Detection
 │
 ▼
Hash Engine
 │
 ▼
Sample Model
 │
 ▼
Metadata Engine
 │
 ▼
Executable Parser
 │
 ▼
Static Analysis
 │
 ▼
IOC Extraction
 │
 ▼
Detection Engine
 │
 ▼
Threat Intelligence
 │
 ▼
Threat Scoring
 │
 ▼
Reporting
 │
 ▼
JSON / HTML / Case Bundle
```

---

# Architectural Boundaries

Each layer communicates only through defined interfaces.

Lower layers do not depend on higher layers.

Examples:

* Hash Engine does not know about Reporting.
* Reporting does not calculate hashes.
* Detection does not parse executable headers.
* File Type Detection does not generate scores.

This separation reduces coupling and improves maintainability.

---

# Extensibility Strategy

The architecture is intentionally prepared for future expansion.

Potential future additions include:

* Plugin framework
* REST API
* Distributed analysis
* Parallel execution
* Sandbox orchestration
* Multi-file correlation
* Digital signature validation
* Certificate trust analysis
* Fuzzy hashing
* Machine-learning-assisted prioritization

These capabilities should integrate into existing layers rather than replacing them.

---

# Architecture Summary

BinaryTriage-X is designed around a central Sample object and a deterministic processing pipeline.

Each module contributes a specific capability.

Each capability produces structured evidence.

Each piece of evidence contributes to explainable findings.

The architecture favors engineering quality, transparency, and long-term evolution over feature accumulation.
