# BrainOS Operational Workflow (The Deterministic Path)

This document serves as the authoritative source of truth for the BrainOS input-to-output flow.

## 🗺️ High-Level Topology
BrainOS operates as a **Star Schema**, not a linear ladder. The `Surgical Router` acts as the hub, instantly dispatching requests to the correct tier based on complexity signatures.

## 🔄 The Deterministic Pipeline

### 1. Entry & Triage
**Path**: `User` $\rightarrow$ `mcp_server.py` $\rightarrow$ `router.py`
- **Process**: The system analyzes the request signature.
- **Decision**: The Router selects a tier (L1-L5) based on the `graph.json` mapping and `Surgical_Cores` configuration.
- **Outcome**: A deterministic assignment of effort and model.

### 2. Surgical Execution
The `BrainExecutor` dispatches the request to the selected tier:
- **L1 (Surgical-Operational)**: Direct, high-precision retrieval.
- **L2 (Functional Logic)**: Dependency tracing and relationship mapping.
- **L3 (Analytical Crunch)**: Structural data transformation using the `LangStruct $\to$ Polars $\to$ DuckDB` pipeline.
- **L4 (Orchestrated Synthesis)**: Complex engineering via `ruflo Swarm` and `LangGraph` self-correcting cycles.
- **L5 (Adversarial Critique)**: A wrapper that executes L4 and then performs an adversarial probe to ensure zero-defect delivery.

### 3. Sovereign Validation (The Gate)
**Path**: `Execution Result` $\rightarrow$ `sovereign.py` $\rightarrow$ `sovereign_state.md`
- **Process**: Every result is gated by the Sovereign State.
- **Validation**: The output is checked against project invariants (the "North Star" rules).
- **Feedback Loop**: If validation fails (`Sovereign_Check == False`), the system triggers a loopback to the L4/L5 execution phase for correction.

### 4. Semantic Delivery
**Path**: `Validated Result` $\rightarrow$ `Surgical Semantic Layer` $\rightarrow$ `User`
- **Process**: Technical extraction results are translated into business-facing definitions.
- **Finality**: The result is delivered to the user.

## 🛠️ Component Map
| Component | File | Role |
| :--- | :--- | :--- |
| **MCP Server** | `src/mcp_server.py` | Entry point & Request handling |
| **Surgical Router** | `src/router.py` | Triage and Tier Assignment |
| **Brain Executor** | `src/executor.py` | Tier-specific logic execution |
| **Sovereign Validator** | `core/sovereign.py` | Invariant enforcement & Guardrails |
| **Config Store** | `src/config.py` | Effort and Model specifications |
| **Sovereign State** | `config/sovereign_state.md` | Root of trust / Project invariants |
