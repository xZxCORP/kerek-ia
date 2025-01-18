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

    year: Optional[int] = None
    owners: Optional[int] = None
    mileage: Optional[int] = None
    mark: Optional[str] = None
    model: Optional[str] = None
