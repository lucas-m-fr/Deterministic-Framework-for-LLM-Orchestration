---
name: l3-example-node
description: Template for L3 Analytical Crunch tasks
metadata:
  tier: L3
  type: analytical
---
# L3 Analytical Node: [DATA_ANALYSIS_TASK]

## 🎯 Objective
Transform raw structural data from [SOURCE] into [INSIGHT].

## 🛠️ Execution Protocol
1. **Extract**: `LangStruct` $\rightarrow$ `CSV/JSON`.
2. **Transform**: `Polars` (Filtering/Aggregation) $\rightarrow$ `DuckDB`.
3. **Validate**: `dbt` test for [SCHEMA_INVARIANT].

## 📌 Pipeline Spec
- Input Schema: [SCHEMA_X]
- Output Metric: [METRIC_Y]
