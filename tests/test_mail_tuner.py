import pytest
import json
from mail_tuner import MailTuner, EmailConfiguration

def test_add_configuration():
    mail_tuner = MailTuner()
    configuration = EmailConfiguration("host", 123, "username", "password")
    mail_tuner.add_configuration(configuration)
    assert len(mail_tuner.get_configurations()) == 1

def test_update_configuration():
    mail_tuner = MailTuner()
    configuration = EmailConfiguration("host", 123, "username", "password")
    mail_tuner.add_configuration(configuration)
    new_configuration = EmailConfiguration("new_host", 456, "new_username", "new_password")
    mail_tuner.update_configuration(0, new_configuration)
    assert mail_tuner.get_configuration(0).host == "new_host"

def test_get_configurations():
    mail_tuner = MailTuner()
    configuration1 = EmailConfiguration("host1", 123, "username1", "password1")
    configuration2 = EmailConfiguration("host2", 456, "username2", "password2")
    mail_tuner.add_configuration(configuration1)
    mail_tuner.add_configuration(configuration2)
    configurations = mail_tuner.get_configurations()
    assert len(configurations) == 2

def test_get_configuration():
    mail_tuner = MailTuner()
    configuration = EmailConfiguration("host", 123, "username", "password")
    mail_tuner.add_configuration(configuration)
    assert mail_tuner.get_configuration(0).host == "host"

def test_save_configurations():
    mail_tuner = MailTuner()
    configuration = EmailConfiguration("host", 123, "username", "password")
    mail_tuner.add_configuration(configuration)
    mail_tuner.save_configurations("configurations.json")
    with open("configurations.json", "r") as file:
        data = json.load(file)
    assert len(data) == 1

def test_load_configurations():
    mail_tuner = MailTuner()
    configuration = EmailConfiguration("host", 123, "username", "password")
    mail_tuner.add_configuration(configuration)
    mail_tuner.save_configurations("configurations.json")
    new_mail_tuner = MailTuner()
    new_mail_tuner.load_configurations("configurations.json")
    assert len(new_mail_tuner.get_configurations()) == 1

def test_index_out_of_range():
    mail_tuner = MailTuner()
    with pytest.raises(IndexError):
        mail_tuner.get_configuration(0)

def test_file_not_found():
    mail_tuner = MailTuner()
    with pytest.raises(FileNotFoundError):
        mail_tuner.load_configurations("non_existent_file.json")
