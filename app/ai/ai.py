import pickle
import pandas as pd

from dto import Vehicle


class KerekAi:
    """
    Model and preprocessor loading
    """

    def __init__(self):
        with open("model.pkl", "rb") as file:
            self.model = pickle.load(file)
            file.close()

        with open("preprocessor.pkl", "rb") as file:
            self.preprocessor = pickle.load(file)
            file.close()

    def execute(self, vehicle: Vehicle) -> bool:
        """_summary_

        Args:
            vehicle (Vehicle): _description_

        Returns:
            bool: True if the vehicle is safe else False
        """
        df = pd.DataFrame([vehicle])

        x_vehicle = self.preprocessor.transform(df)
        vehicle_anomaly_score = self.model.predict(x_vehicle)

        return vehicle_anomaly_score[0] == 1
