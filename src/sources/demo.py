"""Demo source with sample jobs.

Used to test the matching and notification pipeline without any API key.
Replace/remove this once you have configured a real source.
"""
from __future__ import annotations

from datetime import date, timedelta

from models import Job
from sources.base import Source

TODAY = date.today().isoformat()
YESTERDAY = (date.today() - timedelta(days=1)).isoformat()
LAST_WEEK = (date.today() - timedelta(days=6)).isoformat()

SAMPLE_JOBS = [
    Job(
        id="demo:dynamics-365-developer-capgemini",
        title="Dynamics 365 Developer",
        company="CapGemini",
        location="Pune, Maharashtra, IN",
        url="https://example.com/jobs/capgemini-dynamics-365",
        description=(
            "We are hiring a Dynamics 365 Developer to design and develop "
            "model-driven apps and customized D365 Modules (Sales, Service, "
            "Marketing, Field Service). Experience with Power Automate, "
            "plugins, JavaScript and Azure DevOps is required."
        ),
        posted_at=TODAY,
        source="demo",
    ),
    Job(
        id="demo:power-platform-consultant-accenture",
        title="Power Platform Consultant",
        company="Accenture",
        location="Pune / Remote, IN",
        url="https://example.com/jobs/accenture-power-platform",
        description=(
            "Design Power Apps canvas and model-driven apps, Power Automate "
            "flows, and Dataverse solutions. PL-400 certification preferred."
        ),
        posted_at=YESTERDAY,
        source="demo",
    ),
    Job(
        id="demo:d365-crm-developer-infosys",
        title="Senior D365 CRM Developer",
        company="Infosys Ltd.",
        location="Remote, IN",
        url="https://example.com/jobs/infosys-d365-crm",
        description=(
            "Develop Dynamics 365 CRM solutions with plugins, web resources, "
            "and Power FX. Experience with Azure DevOps deployment required."
        ),
        posted_at=TODAY,
        source="demo",
    ),
    Job(
        id="demo:power-apps-developer-tcs",
        title="Power Apps Developer",
        company="TCS",
        location="Bangalore, IN",
        url="https://example.com/jobs/tcs-power-apps",
        description=(
            "Build canvas and model-driven Power Apps applications. "
            "Integrate with SharePoint, Teams and Azure services."
        ),
        posted_at=LAST_WEEK,
        source="demo",
    ),
    Job(
        id="demo:sap-abap-developer",
        title="Senior ABAP Developer",
        company="SAP Labs",
        location="Bangalore, IN",
        url="https://example.com/jobs/sap-abap",
        description=(
            "Develop ABAP code for SAP S/4HANA. CDS Views and AMDP "
            "experience required. No Dynamics experience needed."
        ),
        posted_at=TODAY,
        source="demo",
    ),
    Job(
        id="demo:java-spring-developer",
        title="Java Spring Boot Developer",
        company="Wipro",
        location="Hyderabad, IN",
        url="https://example.com/jobs/wipro-java",
        description=(
            "Develop microservices with Java, Spring Boot and PostgreSQL. "
            "No Microsoft Dynamics experience required."
        ),
        posted_at=TODAY,
        source="demo",
    ),
]


class DemoSource(Source):
    name = "demo"

    def fetch(self, queries):  # noqa: ARG002 - queries ignored for demo data
        return list(SAMPLE_JOBS)
