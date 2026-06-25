import pytest
from mail_tuner import scan_dns_records, DNSRecord
import json

def test_scan_dns_records():
    domain = 'example.com'
    dns_records = [
        DNSRecord('example.com', 'SPF', 'v=spf1 a mx ip4:192.0.2.1 -all'),
        DNSRecord('example.com', 'DKIM', 'v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4Kt6i7L8j7yj'),
        DNSRecord('example.com', 'DMARC', 'v=DMARC1; p=reject; pct=100; rua=mailto:example@example.com; ruf=mailto:example@example.com; fo=1')
    ]

    report = scan_dns_records(domain, dns_records)
    assert report['domain'] == domain
    assert report['findings'] == []

def test_scan_dns_records_missing_spf():
    domain = 'example.com'
    dns_records = [
        DNSRecord('example.com', 'DKIM', 'v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4Kt6i7L8j7yj'),
        DNSRecord('example.com', 'DMARC', 'v=DMARC1; p=reject; pct=100; rua=mailto:example@example.com; ruf=mailto:example@example.com; fo=1')
    ]

    report = scan_dns_records(domain, dns_records)
    assert report['domain'] == domain
    assert len(report['findings']) == 1
    assert report['findings'][0]['mechanism'] == 'SPF'

def test_scan_dns_records_missing_dkim():
    domain = 'example.com'
    dns_records = [
        DNSRecord('example.com', 'SPF', 'v=spf1 a mx ip4:192.0.2.1 -all'),
        DNSRecord('example.com', 'DMARC', 'v=DMARC1; p=reject; pct=100; rua=mailto:example@example.com; ruf=mailto:example@example.com; fo=1')
    ]

    report = scan_dns_records(domain, dns_records)
    assert report['domain'] == domain
    assert len(report['findings']) == 1
    assert report['findings'][0]['mechanism'] == 'DKIM'

def test_scan_dns_records_missing_dmarc():
    domain = 'example.com'
    dns_records = [
        DNSRecord('example.com', 'SPF', 'v=spf1 a mx ip4:192.0.2.1 -all'),
        DNSRecord('example.com', 'DKIM', 'v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4Kt6i7L8j7yj')
    ]

    report = scan_dns_records(domain, dns_records)
    assert report['domain'] == domain
    assert len(report['findings']) == 1
    assert report['findings'][0]['mechanism'] == 'DMARC'

def test_scan_dns_records_empty():
    domain = 'example.com'
    dns_records = []

    report = scan_dns_records(domain, dns_records)
    assert report['domain'] == domain
    assert len(report['findings']) == 3
    assert report['findings'][0]['mechanism'] == 'SPF'
    assert report['findings'][1]['mechanism'] == 'DKIM'
    assert report['findings'][2]['mechanism'] == 'DMARC'
