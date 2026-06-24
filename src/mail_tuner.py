import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class BounceReason(Enum):
    SPF_FAIL = "SPF fail"
    DMARC_POLICY = "DMARC policy"
    CONTENT_FILTER = "Content filter"

@dataclass
class DiagnosticReport:
    probable_causes: List[BounceReason]
    remediation_steps: List[str]

def generate_diagnostic_report(bounce_reason: str) -> DiagnosticReport:
    probable_causes = []
    remediation_steps = []

    if "SPF" in bounce_reason:
        probable_causes.append(BounceReason.SPF_FAIL)
        remediation_steps.append("Check SPF records: https://docs.example.com/spf")
    elif "DMARC" in bounce_reason:
        probable_causes.append(BounceReason.DMARC_POLICY)
        remediation_steps.append("Check DMARC policy: https://docs.example.com/dmarc")
    elif "Content filter" in bounce_reason:
        probable_causes.append(BounceReason.CONTENT_FILTER)
        remediation_steps.append("Check content filter settings: https://docs.example.com/content-filter")

    return DiagnosticReport(probable_causes, remediation_steps)

def generate_pdf_report(report: DiagnosticReport) -> str:
    pdf_content = "Diagnostic Report:\n"
    pdf_content += "Probable causes:\n"
    for cause in report.probable_causes:
        pdf_content += f"- {cause.value}\n"
    pdf_content += "Remediation steps:\n"
    for step in report.remediation_steps:
        pdf_content += f"- {step}\n"
    return pdf_content

def view_report_in_ui(report: DiagnosticReport) -> str:
    ui_content = "Diagnostic Report:<br>"
    ui_content += "Probable causes:<br>"
    for cause in report.probable_causes:
        ui_content += f"- {cause.value}<br>"
    ui_content += "Remediation steps:<br>"
    for step in report.remediation_steps:
        ui_content += f"- {step}<br>"
    return ui_content
