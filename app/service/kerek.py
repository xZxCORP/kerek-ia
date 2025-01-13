from typing import Literal, Optional, Union
from dto import PartialVehicle, Vehicle
from ai import KerekAi
from datetime import datetime


class KerekEngine:
    """
    The Kerek ai
    """

    MEAN_MILEAGE_PER_YEAR = 21000
    CURR_YEAR = datetime.now().year

    def __init__(
        self,
        ai: KerekAi,
        vehicle: Union[Vehicle, PartialVehicle],
        last_vehicle: Optional[Vehicle] = None,
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
        compare_mileage = True if self.vehicle.mileage is not None else False
        compare_years = True if self.vehicle.year is not None else False
        compare_owners = True if self.vehicle.owners is not None else False

        if compare_mileage:
            difference_mileage = self.vehicle.mileage - self.last_vehicle.mileage
            # Lower mileage than before
            if difference_mileage < 0:
                return False
            if compare_years:
                difference_years = self.vehicle.year - self.CURR_YEAR
                # More than the mean mileage
                if difference_mileage > self.MEAN_MILEAGE_PER_YEAR * difference_years:
                    return False
        if compare_owners:
            # Less owners than before
            if self.vehicle.owners < self.last_vehicle.owners:
                return False

        return True
