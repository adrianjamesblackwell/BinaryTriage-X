# Architecture Principles

## Purpose

This document defines the architectural principles that govern every engineering decision made within BinaryTriage-X.

Architecture Decision Records should be evaluated against these principles.

These principles represent long-term engineering values rather than implementation details.

---

# Principle 1

Evidence Before Conclusions

BinaryTriage-X collects evidence before producing findings.

Findings are produced before scores.

Scores are produced before reports.

The system never skips stages.

---

# Principle 2

Explainability Over Automation

Every conclusion must be explainable.

Every score must reference findings.

Every finding must reference evidence.

The platform assists analysts.

It does not replace analyst judgment.

---

# Principle 3

Single Responsibility

Every module performs one primary responsibility.

Modules should remain small, predictable, and independently testable.

---

# Principle 4

Read-Only Analysis

Static analysis never modifies the analyzed sample.

Evidence collection must not alter the original file.

---

# Principle 5

Never Trust Input

Every input is considered hostile.

Validation is mandatory.

Assumptions are prohibited.

---

# Principle 6

Deterministic Processing

The same input under the same configuration should produce the same output.

Random behavior is prohibited.

---

# Principle 7

Explicit Data Flow

Data should flow through documented interfaces.

Hidden dependencies are prohibited.

Global mutable state is prohibited.

---

# Principle 8

Sample-Centric Architecture

Every stage operates on the Sample object.

Analysis data should never become fragmented.

---

# Principle 9

Strong Module Boundaries

Modules communicate only through defined interfaces.

Responsibilities should never overlap.

---

# Principle 10

Evidence is Immutable

Evidence should not change after creation.

Findings reference evidence.

Scores reference findings.

Reports reference scores.

---

# Principle 11

Documentation is Part of the Product

Architecture documentation is considered part of the implementation.

A feature is incomplete until documentation is updated.

---

# Principle 12

Testing is Mandatory

Every public module requires dedicated unit tests.

Architectural decisions should be verifiable.

---

# Principle 13

Security by Default

The safest behavior should always be the default behavior.

Unsafe operations require explicit implementation.

---

# Principle 14

Future Extensibility

Every design decision should consider future expansion.

Future support should not require architectural redesign.

---

# Principle 15

Human Readability

Code is written for engineers.

Readable code is preferred over clever code.

---

# Principle 16

Engineering Over Convenience

Convenience should never replace sound engineering.

Shortcuts that increase long-term maintenance cost should be avoided.

---

# Principle 17

Measure Before Optimizing

Optimization should be based on measurable evidence.

Premature optimization is discouraged.

---

# Principle 18

Architecture Evolves

The architecture is expected to evolve.

Every major change should be documented through an ADR.

Architectural evolution should remain intentional rather than accidental.
