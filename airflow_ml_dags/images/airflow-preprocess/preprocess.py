import os
import click
import pandas as pd


@click.command("preprocess")
@click.option("--input_dir")
@click.option("--output_dir")
def main(input_dir, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "processed_data.csv"), index=False)
    target.to_csv(os.path.join(output_dir, "processed_target.csv"), index=False)


if __name__ == "__main__":
    main()
