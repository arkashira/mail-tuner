import pytest
from mail_tuner import generate_diagnostic_report, generate_pdf_report, view_report_in_ui
from mail_tuner import BounceReason

def test_generate_diagnostic_report_spf():
    bounce_reason = "SPF fail"
    report = generate_diagnostic_report(bounce_reason)
    assert report.probable_causes == [BounceReason.SPF_FAIL]
    assert report.remediation_steps == ["Check SPF records: https://docs.example.com/spf"]

def test_generate_diagnostic_report_dmarc():
    bounce_reason = "DMARC policy"
    report = generate_diagnostic_report(bounce_reason)
    assert report.probable_causes == [BounceReason.DMARC_POLICY]
    assert report.remediation_steps == ["Check DMARC policy: https://docs.example.com/dmarc"]

def test_generate_diagnostic_report_content_filter():
    bounce_reason = "Content filter"
    report = generate_diagnostic_report(bounce_reason)
    assert report.probable_causes == [BounceReason.CONTENT_FILTER]
    assert report.remediation_steps == ["Check content filter settings: https://docs.example.com/content-filter"]

def test_generate_pdf_report():
    report = generate_diagnostic_report("SPF fail")
    pdf_content = generate_pdf_report(report)
    assert "Diagnostic Report:" in pdf_content
    assert "- SPF fail" in pdf_content
    assert "- Check SPF records: https://docs.example.com/spf" in pdf_content

def test_view_report_in_ui():
    report = generate_diagnostic_report("SPF fail")
    ui_content = view_report_in_ui(report)
    assert "Diagnostic Report:" in ui_content
    assert "- SPF fail" in ui_content
    assert "- Check SPF records: https://docs.example.com/spf" in ui_content
