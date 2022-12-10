import os
import pickle
import click
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


@click.command("train")
@click.option("--input_dir")
@click.option("--models_dir")
def main(input_dir, models_dir):
    train_x = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
    train_y = pd.read_csv(os.path.join(input_dir, "train_target.csv"))

    model = RandomForestRegressor(random_state=42)
    model.fit(train_x, train_y)

    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, "model.pkl"), mode="wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()
