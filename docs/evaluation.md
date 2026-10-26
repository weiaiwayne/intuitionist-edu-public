# Evaluation approach

This is an evaluation plan for the framework, not a report of released empirical results.

## Proposed three-condition comparison

The design direction compares:

1. **Baseline:** an agent without the additional acquired skills, memories or protocols.
2. **Acquired experience:** an agent with experience developed through prior human–agent collaboration.
3. **Human-written checklist:** an agent given explicit guidance prepared by a human.

All conditions receive the information needed for the new task. The baseline does not withhold essential task facts, permissions or safety instructions. The checklist comparison asks whether acquired experience adds value beyond readily stated guidance.

Use new tasks whose answers are absent from the retained material. Keep models, tools and working resources comparable, and account for differences in the information supplied. These conditions are a design direction, not a finalized or completed protocol.

For example, a practice about how software stores estimates should be assessed on a new analysis where it matters and another where it should not be applied. Examine whether the agent notices the issue, selects an appropriate check and explains the result. The baseline or checklist may do as well as or better than the experience condition. Additional guidance may constrain exploration or create unnecessary work.

Comparisons separating selected skills or memories are follow-up analyses of which kinds of experience matter, rather than a substitute for the main checklist condition. Task selection, scoring, repeated runs and information controls still need to be specified.

## Other comparisons

Possible comparisons include one agent versus a scoped team; team work with and without peer review; and later tasks with and without access to retained lessons. Keep the task, data access and evaluation criteria comparable. Report prior exposure and changes in model or prompt configuration.

## Measure the intended outcome

| Dimension | Examples of evidence |
| --- | --- |
| Task quality | Blinded assessment against declared criteria |
| Scientific validity | Independent labels, justified methods, verified inference |
| Coordination | Unnecessary handoffs, duplicated work, unauthorized participation |
| Cost and time | Recorded tokens, elapsed time, compute and human attention |
| Error correction | Reproduced baseline, bounded repair, dependent outputs checked |
| Learning and transfer | Correct retrieval and application in later eligible tasks |
| Human control | Scope changes and acceptance decisions attributed correctly |

A faster task is not necessarily better research. More agreement among agents is not necessarily greater validity. Separate process success, implementation correctness and empirical support.

## Report uncertainty and limitations

Match the analysis unit and uncertainty calculation to the data. For repeated observations from a person or source, consider dependence rather than assuming rows are independent. Compare models on paired observations when the scientific question requires it.

Distinguish proxy outcomes from the construct of interest. High prediction performance against an algorithm-defined label does not establish validity against an independently measured target.

## Evidence needed before claiming learning

Record the initial decision, available context, feedback, retained lesson, later retrieval and later outcome. Evaluate transfer on work not used to create the lesson. Use a baseline, examine negative transfer, and report cases where the mechanism added cost without benefit.

No released dataset or benchmark in this repository currently establishes those effects.
