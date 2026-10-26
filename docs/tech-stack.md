# Tech stack

The development system combines an agent runtime, a conversation interface, file-based coordination and research tools. These are technology choices in the current development approach, not mandatory dependencies for reading or adapting this public framework.

| Component | Role | Public-release status |
| --- | --- | --- |
| Hermes Agent | Agent runtime and tool-mediated execution | External dependency; private profiles and customizations are not shipped |
| Discord | Human-agent conversation and task notifications | Interface described; no server IDs, bot identities or tokens provided |
| Language model endpoints | Reasoning, drafting, coding and review | Providers and models are replaceable; no API keys or live endpoint settings included |
| Python | Coordination utilities, data handling and validation | Private implementation not distributed in this release |
| Shell and operating-system services | Launching and supervising background work | No production commands or service configurations included |
| Markdown | Human-readable briefs, reports, memory and skills | Public documentation uses Markdown |
| JSON, JSONL and YAML | Structured state, records and configuration | Formats described; no live records/configuration included |
| Git and GitHub | Version control and the public research companion | This repository contains a separately curated public history |
| Task-specific analysis packages | Statistical analysis, measurement and reporting | No study environment or empirical dependencies claimed reproducible here |

## Models and roles

The development approach has used model families from several providers, including GLM, MiniMax, Kimi and DeepSeek. Exact models, effort settings and routing can change. This release does not freeze or certify any particular production configuration.

An assignment can designate a lead, drafter, coder, reviewer or synthesizer. The role is not inherent in a model. An external reviewer can provide another implementation or audit, with prior exposure and method differences disclosed.

For a future executable research release, record exact model identifiers, provider, access date, effort settings, prompts, sampling settings and software versions. A brand name is not sufficient for reproducibility.

## Research tooling

Research tasks may use Python packages such as NumPy, pandas, SciPy and scikit-learn; some tasks use transformer libraries or model-specific tooling. Their use depends on the task. This repository does not publish a requirements file because it does not ship an operational research pipeline.

## Upstream resources

- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Discord developer documentation](https://discord.com/developers/docs/intro)
- [Python documentation](https://docs.python.org/3/)
- [Git documentation](https://git-scm.com/doc)

Use the upstream installation instructions and licenses for those projects. Naming a dependency does not imply endorsement or transfer its license to this repository.
