from dto import Vehicle
from ai import KerekAi


class KerekEngine:
    """
    The Kerek ai
    """

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.reason = "Ce véhicule n'est pas dans les normes."

    def execute(self):
        ai = KerekAi()
        is_safe = ai.execute(self.vehicle)

        return None if is_safe else self.reason
