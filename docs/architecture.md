# Architecture

The framework separates interaction, task coordination, artifacts, model execution and human authority. This is a conceptual map of the development approach, not a deployable installation specification.

![Conceptual architecture](../assets/framework.svg)

| Layer | Responsibility | Boundary |
| --- | --- | --- |
| Human direction | Purpose, task scope, access, final decisions | Agent suggestions do not become human approval automatically |
| Interaction | Receive questions and route task messages | A conversational acknowledgment is not proof of execution |
| Coordination | Assign participants, phases, completion conditions and handoffs | Participation follows task scope |
| Agent execution | Read assigned context, use tools and produce work | Tool success does not establish scientific validity |
| Artifact workspace | Store briefs, drafts, reviews, outputs and revisions | Evidence and supersession remain inspectable |
| Memory and skills | Retain context and reusable judgment | Retention is not proof of learning or authority |
| Review and evaluation | Check methods, evidence, dependence and outcomes | Agreement alone is not validation |

## A typical flow

1. The human defines a task and its intended use.
2. The task names participants and deliverables.
3. Participants work within the assigned scope and record what they saw.
4. A reviewer inspects the work and supporting artifacts.
5. Revisions address specific issues and preserve the correction trail.
6. A human accepts, rejects or redirects the work.
7. Candidate lessons are retained with scope and evidence, then evaluated in later use.

Not every small task needs multiple agents or all seven steps. The amount of coordination should match the consequence and complexity of the work.

## Independence

For an independent coding or judgment comparison, record which prompts, data, prior outputs and discussions each participant could access. Separate runs on different models do not guarantee independence. Shared assumptions, examples and prior exposure can produce correlated errors.

## Public implementation boundary

This repository does not distribute production gateway extensions, agent profiles, private configurations, service definitions, model credentials or operational logs. The stack describes the components; it does not reproduce their private wiring.
