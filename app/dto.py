from pydantic import BaseModel
from typing import Optional


class Vehicle(BaseModel):
    """_summary_
    Vehicle Dto to analyze
    """

    year: int
    owners: int
    mileage: int
    mark: str
    model: str


class PartialVehicle(BaseModel):
    """_summary_
    Vehicle Dto to analyze
    """

    year: Optional[int]
    owners: Optional[int]
    mileage: Optional[int]
    mark: Optional[str]
    model: Optional[str]
