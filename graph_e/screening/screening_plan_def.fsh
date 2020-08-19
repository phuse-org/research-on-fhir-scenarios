Instance: Screening
InstanceOf: PlanDefinition

// Name
* name = "Screening"
* title = "Screening Visit" 
* status.system = "http://hl7.org/fhir/publication-status"
* status.code = #draft "draft"

// Informed Consent
* action[0].title = "Informed Consent"
* action[0].description = "Gather informed Consent"
* action[0].definitionCanonical = InformedConsent

