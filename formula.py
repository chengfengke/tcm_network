class Formula:
    def __init__(self, hvp_id, name, herbs):
        self.hvp_id = hvp_id
        self.name = name
        self.herbs = herbs  # List of Herb objects

    def __repr__(self):
        return f"Formula(hvp_id={self.hvp_id}, name={self.name}, herbs=[{', '.join([herb.name for herb in self.herbs])}])"