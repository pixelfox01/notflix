class Movie:
    def __init__(self, name, duration, lead_actor):
        self.name = name
        self.duration = duration
        self.lead_actor = lead_actor

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_lead_actor(self):
        return self.lead_actor
