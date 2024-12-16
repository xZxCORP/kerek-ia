from dto import Vehicle
from ai import KerekAi


class KerekEngine:
    """
    The Kerek ai
    """

    def __init__(self, vehicle: Vehicle, ai: KerekAi):
        self.vehicle = vehicle
        self.reason = "Ce véhicule n'est pas dans les normes."
        self.ai = ai

    def execute(self):
        is_safe = self.ai.execute(self.vehicle)

        return None if is_safe else self.reason
