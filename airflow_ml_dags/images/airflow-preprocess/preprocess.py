import os
import click
import pandas as pd


TRAIN_TYPE = "train"
TEST_TYPE = "test"


@click.command("preprocess")
@click.option("--input_dir")
@click.option("--output_dir")
@click.option("--data_type")
def main(input_dir, output_dir, data_type):
    os.makedirs(output_dir, exist_ok=True)

    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    data.to_csv(os.path.join(output_dir, "processed_data.csv"), index=False)

    if data_type == TRAIN_TYPE:
        target = pd.read_csv(os.path.join(input_dir, "target.csv"))
        target.to_csv(os.path.join(output_dir, "processed_target.csv"), index=False)
    elif data_type == TEST_TYPE:
        pass
    else:
        raise NotImplementedError(f"Data type hasn't valid value: {data_type}")


if __name__ == "__main__":
    main()
