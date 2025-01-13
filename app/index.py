import traceback

from ai import KerekAi
from fastapi import FastAPI

from service.kerek import KerekEngine
from dto import Vehicle, PartialVehicle

api = FastAPI()
# Load the ai at start
ai = KerekAi()


@api.get("/status")
def status():
    return {"status": 200}


@api.post("/predict/analyze")
def predict_analyze(vehicle: Vehicle):
    """_summary_

    Args:
        vehicle (Vehicle)

    Raises:
        e: error

    Returns:
        _type_: string or null
    """

    try:
        output = KerekEngine(ai, vehicle, None, "analyze").execute()

        return output
    except Exception as e:
        traceback.print_exc(e)
        raise e


@api.post("/predict/compare")
def predict_compare(vehicle: PartialVehicle, last_vehicle: Vehicle):
    """_summary_

    Args:
        vehicle (Vehicle)

    Raises:
        e: error

    Returns:
        _type_: string or null
    """

    try:
        output = KerekEngine(ai, vehicle, last_vehicle, "compare").execute()

        return output
    except Exception as e:
        traceback.print_exc(e)
        raise e
