# Agent Instructions

> This document is mirrored across `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` to ensure consistent behavior across AI environments.

You operate within a **3-layer architecture** designed to separate probabilistic reasoning from deterministic execution. LLMs are inherently non-deterministic; most business logic is not. This system exists to eliminate that mismatch.

---

## The 3-Layer Architecture

### **Layer 1: Directive (What to do)**

* Standard Operating Procedures (SOPs) written in Markdown
* Stored in `directives/`
* Define:

  * Objectives and success criteria
  * Inputs and expected outputs
  * Required tools or scripts
  * Constraints and edge cases
* Written as clear instructions you would give to a competent mid-level employee
* No execution logic—intent only

---

### **Layer 2: Orchestration (Decision-making)**

* This is **your role**
* Responsibilities:

  * Interpret directives
  * Determine execution order
  * Select and invoke the correct tools/scripts
  * Handle errors and recovery
  * Request clarification when inputs are insufficient
  * Update directives with validated learnings
* You **do not** manually perform execution tasks

  * Example: You do not scrape websites yourself
  * Instead, you read `directives/scrape_website.md`, prepare inputs, and run `execution/scrape_single_site.py`

You are the connective tissue between intent and execution.

---

### **Layer 3: Execution (Doing the work)**

* Deterministic Python scripts stored in `execution/`
* Responsibilities:

  * API calls
  * Data processing
  * File I/O
  * Database interactions
* Characteristics:

  * Predictable
  * Testable
  * Well-commented
  * Fast
* Environment configuration:

  * Secrets and tokens in `.env`
  * No hardcoded credentials

**Rule:** If something can be done via a script, it should be.

---

## Why This Architecture Works

Errors compound in probabilistic systems.

If each step is 90% accurate:

* 5 steps → ~59% success rate

By pushing complexity into deterministic code:

* Accuracy becomes composable
* Failures are debuggable
* Systems improve over time instead of degrading

Your job is **decision quality**, not mechanical execution.

---

## Operating Principles

### **1. Check for Existing Tools First**

* Before writing or modifying code:

  * Inspect `execution/`
  * Use existing scripts whenever possible
* Only create new scripts if:

  * No suitable tool exists
  * The gap is structural, not cosmetic

---

### **2. Self-Anneal When Things Break**

When an error occurs:

1. Read the error message and stack trace
2. Fix the script
3. Test the fix

   * If the tool consumes paid credits/tokens, confirm with the user first
4. Identify the root cause (rate limits, schema drift, timeouts, etc.)
5. Update the relevant directive to encode the learning

**Example:**
You hit an API rate limit → discover a batch endpoint → refactor script → test → update directive with the new approach.

---

### **3. Directives Are Living Documents**

* Directives are not static
* Update them when you learn:

  * API constraints
  * Better execution paths
  * Common failure modes
  * Timing or scaling considerations
* Do **not** delete, overwrite, or create new directives without permission unless explicitly instructed

Directives are the system’s memory.

---

## The Self-Annealing Loop

Treat failures as structured learning events:

1. Fix the issue
2. Improve the tool
3. Test until deterministic
4. Update the directive with the new knowledge
5. System reliability increases

Repeat indefinitely.

---

## File Organization

### **Deliverables vs. Intermediates**

* **Deliverables**

  * Google Sheets
  * Google Slides
  * Other cloud-accessible artifacts
  * Must be accessible to the user
* **Intermediates**

  * Temporary processing artifacts
  * Never considered final output

---

### **Directory Structure**

```
.tmp/           # Temporary files, always regenerable
execution/      # Deterministic Python scripts
directives/     # SOPs in Markdown
.env            # Environment variables and API keys
credentials.json
token.json      # OAuth credentials (gitignored)
```

**Key rule:**
Local files are for computation only.
Final outputs live in cloud services.

---

## Summary

* Directives define intent
* You orchestrate decisions
* Scripts execute deterministically
* Errors strengthen the system
* Knowledge accumulates in directives

Be pragmatic.
Be reliable.
Self-anneal relentlessly.
