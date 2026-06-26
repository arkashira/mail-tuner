import json
from dataclasses import dataclass
from typing import List

@dataclass
class EmailConfiguration:
    """Dataclass to hold email configuration"""
    host: str
    port: int
    username: str
    password: str

class MailTuner:
    """Class to manage email configurations"""
    def __init__(self):
        self.configurations = []

    def add_configuration(self, configuration: EmailConfiguration):
        """Add a new email configuration"""
        self.configurations.append(configuration)

    def update_configuration(self, index: int, configuration: EmailConfiguration):
        """Update an existing email configuration"""
        if index < len(self.configurations):
            self.configurations[index] = configuration
        else:
            raise IndexError("Index out of range")

    def get_configurations(self) -> List[EmailConfiguration]:
        """Get all email configurations"""
        return self.configurations

    def get_configuration(self, index: int) -> EmailConfiguration:
        """Get a specific email configuration"""
        if index < len(self.configurations):
            return self.configurations[index]
        else:
            raise IndexError("Index out of range")

    def save_configurations(self, filename: str):
        """Save email configurations to a file"""
        data = []
        for configuration in self.configurations:
            data.append({
                "host": configuration.host,
                "port": configuration.port,
                "username": configuration.username,
                "password": configuration.password
            })
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_configurations(self, filename: str):
        """Load email configurations from a file"""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for configuration in data:
                self.configurations.append(EmailConfiguration(
                    host=configuration["host"],
                    port=configuration["port"],
                    username=configuration["username"],
                    password=configuration["password"]
                ))
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
