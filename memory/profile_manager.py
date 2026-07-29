from memory.profile import profile


class ProfileManager:

    def set(self, key: str, value):

        if hasattr(profile, key):

            setattr(profile, key, value)

    def get(self, key: str):

        return getattr(profile, key)

    def show(self):

        return profile


manager = ProfileManager()