from mail_tuner import EmailConfiguration, analyze_email_configuration, provide_recommendations, integrate_with_deliverability_features

def test_analyze_email_configuration():
    config = EmailConfiguration('smtp.example.com', 587, True, 'username', 'password')
    analysis = analyze_email_configuration(config)
    assert analysis == {}

    config = EmailConfiguration('smtp.example.com', 25, False, 'username', 'password')
    analysis = analyze_email_configuration(config)
    assert analysis == {
        'smtp_port': 'Non-standard SMTP port, consider using 587',
        'tls_enabled': 'TLS is not enabled, consider enabling it for security'
    }

def test_provide_recommendations():
    analysis = {
        'smtp_port': 'Non-standard SMTP port, consider using 587',
        'tls_enabled': 'TLS is not enabled, consider enabling it for security'
    }
    recommendations = provide_recommendations(analysis)
    assert recommendations == [
        'Fix smtp_port: Non-standard SMTP port, consider using 587',
        'Fix tls_enabled: TLS is not enabled, consider enabling it for security'
    ]

def test_integrate_with_deliverability_features():
    config = EmailConfiguration('smtp.example.com', 587, True, 'username', 'password')
    analysis = analyze_email_configuration(config)
    deliverability_features = integrate_with_deliverability_features(config, analysis)
    assert deliverability_features == {
        'email_configuration': {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'tls_enabled': True,
            'username': 'username',
            'password': 'password'
        },
        'analysis': {},
        'recommendations': []
    }
