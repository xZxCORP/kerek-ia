from pydantic import BaseModel


class Vehicle(BaseModel):
    """_summary_
    Vehicle Dto to analyze
    """

    year: int
    owners: int
    mileage: int
    mark: str
    model: str
