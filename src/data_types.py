from dataclasses import dataclass


@dataclass
class UserData:  # Типо DTO
    source: str
    name: str
    email: str
    sex: str

    def to_tuple(self):
        return self.source, self.name, self.email, self.sex
