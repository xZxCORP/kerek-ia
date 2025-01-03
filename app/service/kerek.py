from typing import Literal, Union
from dto import Vehicle
from ai import KerekAi


class KerekEngine:
    """
    The Kerek ai
    """

    MEAN_MILEAGE_PER_YEAR = 21000
    CURR_YEAR = 2025

    def __init__(
        self,
        ai: KerekAi,
        vehicle: Vehicle,
        last_vehicle: Union[Vehicle, None] = None,
        objective: Literal["compare", "analyze"] = "analyze",
    ):
        self.vehicle = vehicle
        self.last_vehicle = last_vehicle
        self.reason = "Ce véhicule n'est pas dans les normes."
        self.ai = ai
        self.objective = objective

    def execute(self):
        """Executes the service

        Returns:
            _type_: _description_
        """
        is_safe = self.ai.execute(self.vehicle)

        if self.objective == "compare":
            is_safe = self._compare()

        output = {"anomaly": not is_safe, "reason": None if is_safe else self.reason}
        return output

    def _compare(self):
        difference_mileage = self.vehicle.mileage - self.last_vehicle.mileage
        difference_years = self.vehicle.year - self.CURR_YEAR

        # Lower mileage than before
        if difference_mileage < 0:
            return False
        # More than the mean mileage
        if difference_mileage > self.MEAN_MILEAGE_PER_YEAR * difference_years:
            return False
        # Less owners than before
        if self.vehicle.owners < self.last_vehicle.owners:
            return False

        return True
