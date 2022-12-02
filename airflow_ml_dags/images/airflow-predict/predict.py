import os
import pickle
import click
import pandas as pd


@click.command("predict")
@click.option("--input_dir")
@click.option("--output_dir")
@click.option("--model_path")
def main(input_dir, output_dir, model_path):
    data = pd.read_csv(os.path.join(input_dir, "processed_data.csv"))

    with open(model_path, mode="rb") as file:
        model = pickle.load(file)

    predictions = model.predict(data)
    predictions = pd.DataFrame(data=predictions, columns=['target'])

    os.makedirs(output_dir, exist_ok=True)
    predictions.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)


if __name__ == "__main__":
    main()
