# CLAUDE.md - Global Master Guide

## 🗺️ BRAIN TOPOLOGY
This is the central node. All operational contexts branch from here:

- **Work Branch**: `[PATH_TO_WORK_BRANCH]/CLAUDE.md`
- **Personal Branch**: `[PATH_TO_PERSONAL_BRANCH]/CLAUDE.md`
- **Projects Branch**: `[PATH_TO_PROJECTS_BRANCH]/CLAUDE.md`

## 🛡️ CORE DIRECTIVES
- **Local Operation**: Running locally via Local-LLM. No cloud dependencies.
- **The Wall**: Maintain absolute, zero-compromise separation between the Work Branch and the Personal Branch.
- **File Hygiene**: All work, scripts, and data assets MUST be stored in designated project directories on the designated drive.

## 🧠 MEMORY & STATE
- **Permanent Memory**: Authoritative source for all long-term facts: `[PATH_TO_PERMANENT_MEMORY]\`
- **Context Management**: Prioritize lean context.

## ⚙️ OPERATIONAL FRAMEWORK (Surgical Agent)
When operating within the Work Branch, adhere to the **Work Brain OS**:
- **Surgical Routing**: Map requests to complexity tiers (L1-L5).
- **L1 Fast-Path**: For Surgical-Operational (L1) tasks, direct lookup/edit is permitted if target node metadata is cached.
- **Execution Flow**: Graph $\rightarrow$ Node $\rightarrow$ Surgical Read $\rightarrow$ SkillOpt Evolution.
- **Data Pipeline**: Use `LangStruct` $\rightarrow$ `Polars` $\rightarrow$ `DuckDB` $\rightarrow$ `dbt`.
- **Verification**: No skill is executed "blind." JIT-read the relevant Brain node.

## 🛠️ CODING GUIDELINES
- **Think Before Coding**: State assumptions explicitly. Surface tradeoffs.
- **Simplicity First**: Minimum code that solves the problem.
- **Surgical Changes**: Touch only what you must. Match existing style exactly.
- **Goal-Driven Execution**: Transform tasks into verifiable goals.
