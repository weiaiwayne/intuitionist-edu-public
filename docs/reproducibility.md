# Availability and reproducibility

This first public release makes the framework and technology choices inspectable. It does not contain the private runtime, agent histories, study data, model prompts from actual studies, analysis code or empirical results.

Readers can reproduce the documentation build as ordinary Markdown and inspect the included SVG. The small repository-checking utility uses only Python's standard library. It checks the release package; it is not a demonstration of agent orchestration or research performance.

## Levels of availability

| Material | Available here? |
| --- | --- |
| Project overview and conceptual framework | Yes |
| Tech stack and workflow description | Yes |
| Evaluation questions and known boundaries | Yes |
| Production installation and configuration | No |
| Executable agent-team prototype | No |
| Original study replication package | No |
| Research datasets or model checkpoints | No |
| Public archival DOI | Not yet assigned |

## What an executable release would need

A separately reviewed prototype should include setup instructions, controlled inputs, expected outputs, environment requirements and a documented test. An empirical reproduction package also needs the relevant protocol, model settings, data rights and access steps, analysis code and provenance.

Synthetic data can illustrate a workflow. It cannot automatically reproduce findings from restricted real data. Any future synthetic artifact must state which insights it reproduces and which it does not.

## Stable references

Cite a release or commit, not only the moving default branch. A future archive can preserve that exact release and supply a DOI. No DOI or journal acceptance should be implied before it exists. See [citation guidance](../CITATION.md).
