from dataclasses import dataclass, field


@dataclass
class UserProfile:

    name: str = ""

    occupation: str = ""

    company: str = ""

    location: str = ""

    email: str = ""

    phone: str = ""

    preferences: dict = field(default_factory=dict)


profile = UserProfile()