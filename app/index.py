import traceback

from fastapi import FastAPI

from service.kerek import KerekEngine
from dto import Vehicle

api = FastAPI()


@api.get("/status")
def status():
    return {"status": 200}


@api.post("/predict")
def predict_anomaly(vehicle: Vehicle):
    """_summary_

    Args:
        vehicle (Vehicle)

    Raises:
        e: error

    Returns:
        _type_: string or null
    """

    try:
        output = KerekEngine(vehicle).execute()

        return output
    except Exception as e:
        traceback.print_exc(e)
        raise e
