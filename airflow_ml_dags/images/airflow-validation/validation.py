import os
import pickle
import click
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error


def _get_metrics_df(rmse, mae):
    columns = ["metric", "value"]
    rows = [
        {"metric": "rmse", "value": rmse},
        {"metric": "mae", "value": mae},
    ]

    return pd.DataFrame(data=rows, columns=columns)


@click.command("validate")
@click.option("--input_dir")
@click.option("--output_dir")
@click.option("--models_dir")
def main(input_dir, output_dir, models_dir):
    validation_x = pd.read_csv(os.path.join(input_dir, "validation_data.csv"))
    validation_y = pd.read_csv(os.path.join(input_dir, "validation_target.csv"))

    with open(os.path.join(models_dir, "model.pkl"), mode="rb") as file:
        model = pickle.load(file)

    predictions = model.predict(validation_x)

    rmse = np.sqrt(mean_squared_error(validation_y, predictions))
    mae = mean_absolute_error(validation_y, predictions)

    metrics = _get_metrics_df(rmse, mae)
    os.makedirs(output_dir, exist_ok=True)
    metrics.to_csv(os.path.join(output_dir, "metrics.csv"), index=False)


if __name__ == "__main__":
    main()
