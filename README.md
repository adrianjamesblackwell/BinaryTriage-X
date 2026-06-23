# BinaryTriage-X

**BinaryTriage-X** is a static binary triage platform designed to reduce the time required to assess unknown PE and ELF executables.

The project focuses on fast, explainable, and reproducible risk assessment for malware analysts, incident responders, reverse engineers, SOC teams, and security researchers.

## Mission

Unknown binaries create operational uncertainty.

BinaryTriage-X helps answer:

* What is this binary?
* Is it suspicious?
* Why is it suspicious?
* What should an analyst investigate first?
* How should this sample be prioritized?

The platform does not claim that a file is malware.
Instead, it provides investigation priority based on observable static indicators.

## Initial Scope

Version 1 focuses on static analysis.

Supported formats:

* PE
* ELF

Core capabilities:

* File metadata extraction
* Cryptographic hashing
* Entropy analysis
* Import analysis
* Section analysis
* String extraction
* Packer indicators
* Suspicious indicator scoring
* Risk and priority assessment
* JSON reporting
* CLI interface

## Design Principles

BinaryTriage-X is designed around the following principles:

1. Safety first: samples are not executed.
2. Explainability: every score must have a reason.
3. Reproducibility: same input should produce the same output.
4. Analyst usefulness: results must help prioritization.
5. Extensibility: new rules and formats should be easy to add.
6. Measurability: performance and detection quality should be testable.

## Current Status

Project stage:

```text
v0.1 — Architecture and File Identity Engine
```

Current focus:

* Repository structure
* Documentation foundation
* File hashing
* Metadata extraction
* JSON report schema

## Safety Notice

This repository does not distribute malware samples.

Any malware analysis should be performed only in a controlled, isolated, and legally authorized environment.

Do not execute unknown binaries on a host machine.

## Roadmap

| Version | Goal                                        |
| ------- | ------------------------------------------- |
| v0.1    | Architecture, repository structure, hashing |
| v0.2    | Metadata, entropy, strings                  |
| v0.3    | PE static analysis                          |
| v0.4    | ELF static analysis                         |
| v0.5    | Suspicious indicators                       |
| v0.6    | Explainable scoring engine                  |
| v0.7    | JSON reporting                              |
| v0.8    | Evaluation framework                        |
| v0.9    | Analyst-ready CLI                           |
| v1.0    | Stable static triage release                |

## License

To be determined.
