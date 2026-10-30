# 🧠 BRAINOS: THE COMPLETE LEGACY ARCHIVE
**Status**: System Hibernation / Master Backup
**Date**: 2026-10-30
**Version**: 2.1 (Final Stable)

---

## 1. EXECUTIVE SUMMARY: THE COGNITIVE OS
BrainOS is not a software application; it is a **Deterministic Cognitive Operating System**. It is designed to shift LLM interactions from probabilistic "guessing" to a surgically precise, tiered routing system. 

The goal of this system is **Zero-Defect Delivery**. It achieves this by decoupling the "Thinking" (The Persona) from the "Doing" (The Infrastructure) and gating everything through a "Sovereign State" of absolute truth.

---

## 2. THE COGNITIVE LAYER (The Persona)
The system is governed by the **Surgical Agent Persona**, defined in `CLAUDE.md` and `SYSTEM.md`. This layer acts as the "Frontal Lobe" of the system.

### 🛡️ Core Directives
- **The Wall**: Absolute separation between Work and Personal knowledge branches.
- **Local Operation**: Zero-compromise local execution to ensure privacy and speed.
- **File Hygiene**: Strict storage protocols to prevent data fragmentation.

### 🛠️ Behavioral Guidelines (The Filters)
Every action taken by the Brain must pass through these four filters:
1. **Think Before Coding**: Surface tradeoffs, state assumptions, and avoid silent decisions.
2. **Simplicity First**: Minimum viable code. No speculative abstractions.
3. **Surgical Changes**: Touch only what is broken. Match existing style exactly.
4. **Goal-Driven Execution**: Transform every task into a verifiable goal before starting.

---

## 3. THE DETERMINISTIC ARCHITECTURE (The BrainOS)
The system operates as a **Star Schema** where a central router dispatches requests to specific complexity tiers.

### 🏗️ The 5-Tier Surgical Framework
| Tier | Name | Goal | Pipeline | Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **L1** | Surgical-Operational | Instant Retrieval | Graphify $\to$ Surgical Read | Deterministic Fact |
| **L2** | Functional Logic | Dependency Mapping | Graphify BFS $\to$ Logic Trace | Dependency Map |
| **L3** | Analytical Crunch | Data Transformation | LangStruct $\to$ Polars $\to$ DuckDB $\to$ dbt | Structured Report |
| **L4** | Orchestrated Synthesis | Complex Engineering | ruflo Swarm $\to$ DeepAgent $\to$ LangGraph | Synthesized Solution |
| **L5** | Adversarial Critique | Zero-Defect Delivery | L4 Baseline $\to$ Adversarial Probe $\to$ Rubric | Verified Delivery |

### 🔄 The Operational Loop
`Request` $\to$ `Surgical Router` $\to$ `Tier Selection` $\to$ `Brain Executor` $\to$ `Sovereign Validator` $\to$ `Surgical Semantic Layer` $\to$ `User`.

---

## 4. THE TECHNICAL INFRASTRUCTURE (The Plumbing)
### 🔌 The MCP Layer
The system utilizes the **Model Context Protocol (MCP)** to bridge the gap between the LLM's reasoning and the local machine's capabilities.
- **mcp_server.py**: The gateway that exposes the `brain_route` and `brain_execute` tools.
- **executor.py**: The engine that handles the actual dispatching to the L1-L5 pipelines.
- **router.py**: The triage center that uses `graph.json` and `config.py` to assign tiers.

### 🛠️ The Analytical Stack (The Muscle)
For L3 and L4 tasks, the system employs a high-performance data pipeline:
- **LangStruct**: For schema-based, grounded extraction.
- **Polars**: For lightning-fast data manipulation.
- **DuckDB**: For complex SQL-based analytical queries.
- **dbt**: For data transformation and quality testing.

---

## 5. THE GUARDRAIL SYSTEM (The Root of Trust)
The most critical component of BrainOS is the **Sovereign State**.

- **Sovereign Validator (`sovereign.py`)**: A boolean gate that validates every single output against the `sovereign_state.md` file.
- **Sovereign State (`sovereign_state.md`)**: A list of absolute project invariants (e.g., "All SQL must be Snowflake dialect").
- **The Feedback Loop**: If the validator returns `False`, the system triggers a mandatory loopback to the Agent for correction. This eliminates "hallucination drift."

---

## 6. THE KNOWLEDGE LAYER (The Wiki)
The Brain is fueled by a modular knowledge base stored in Markdown.
- **Surgical Nodes**: Tiered files that contain specific protocols and knowledge.
- **Semantic Layer**: A translation layer that converts technical extraction (e.g., "Entity_ID: 123") into business-ready language (e.g., "Customer: Acme Corp").

---

## 7. REPLICATION & WAKE-UP GUIDE
To resume this system with a new LLM, follow these steps:

### Step 1: Setup the Environment
1. Clone the GitHub Repository.
2. Initialize the `Surgical Brain` directory on the designated drive (D:).
3. Configure the MCP server and provide the necessary API keys via the **Global Vault**.

### Step 2: Initialize the Persona
1. Load the `CLAUDE_GLOBAL_TEMPLATE.md` and `CLAUDE_WORK_TEMPLATE.md` into the new LLM's system prompt or project instructions.
2. Ensure the agent understands the **Cognitive Filters** (Think, Simplify, Surgical, Goal-Driven).

### Step 3: Map the Brain
1. Run the `boot.py` sequence to verify the `Symmetry Check`.
2. Ensure the `graph.json` is correctly mapping the current knowledge nodes to the L1-L5 tiers.

### Step 4: Test the Loop
1. Submit a known L1 request $\to$ Verify direct retrieval.
2. Submit a known L3 request $\to$ Verify Polars/DuckDB execution.
3. Submit a "non-sovereign" request $\to$ Verify that the `Sovereign Validator` catches the error and loops back.

---

## 8. FINAL ARCHITECTURAL MAP (Mermaid)
[The architecture_map.mermaid file in the repository is the authoritative visual representation of this system.]

**End of Legacy Archive.**
