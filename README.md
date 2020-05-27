# research-on-fhir-scenarios
Scenarios for the PhUSE Research on FHIR Protocol expansion

# Scenarios 
* ResearchStudy (Graph 0)
* Versioning (Graph G)
    * Workflow
    * Protocol Amendment
* Trial Design
    * Arms
* Schedule of Activities
    * Epochs (Graph A) [epochs](./graph_a/epochs.json)
        * Screening
        * Treatment
        * Follow-up
        * Arms
    * Encounters
        * Scheduled Events (Visits) (Graph B) [scheduled_events](./graph_b/scheduled_events.json)
        * Unscheduled Events (Graph C) [unscheduled_events](./graph_c/unscheduled_events.json)
        * Continuous Events (eg mHealth) (Graph D) [continuous_events](./graph_c/continuous_events.json)
    * Triggers/Transitions
        * Scheduled Transitions (eg Visit 1 → Visit 2, Randomization etc) (Graph B1)
        * Unscheduled Transitions (eg Adverse Events) (Graph C1)
        * Should include ranges, relative events, etc
    * Planned Observations on the Patient (eg Questionnaires, Procedures)
        * Defining (Graph E) [defined_events](./graph_e/defined_events.json)
        * Planning (Graph F) [planned_events](./graph_f/planned_events.json)
* Eligibility
    * Condition
    * Age
    * Gender
    * Verbatim text (inclusion/exclusion)


