import os
import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command("split")
@click.option("--input_dir")
@click.option("--output_dir")
def main(input_dir, output_dir):
    processed_data = pd.read_csv(os.path.join(input_dir, "processed_data.csv"))
    processed_target = pd.read_csv(os.path.join(input_dir, "processed_target.csv"))

    train_x, validation_x, train_y, validation_y = train_test_split(
        processed_data,
        processed_target,
        random_state=42,
        test_size=0.33
    )

    os.makedirs(output_dir, exist_ok=True)
    train_x.to_csv(
        os.path.join(output_dir, "train_data.csv"), index=False
    )
    train_y.to_csv(
        os.path.join(output_dir, "train_target.csv"), index=False
    )
    validation_x.to_csv(
        os.path.join(output_dir, "validation_data.csv"), index=False
    )
    validation_y.to_csv(
        os.path.join(output_dir, "validation_target.csv"), index=False
    )


if __name__ == "__main__":
    main()
