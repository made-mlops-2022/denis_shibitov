import os
import click
import pandas as pd
from sklearn.datasets import load_diabetes


def generate_data():
    source_data = load_diabetes()
    data = pd.DataFrame(
        data=source_data['data'],
        columns=source_data['feature_names']
    )

    target = pd.DataFrame(
        data=source_data['target'],
        columns=['target']
    )

    return data, target


@click.command()
@click.argument("output_dir")
def main(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    data, target = generate_data()
    data.to_csv(os.path.join(output_dir, 'data.csv'), index=False)
    target.to_csv(os.path.join(output_dir, 'target.csv'), index=False)


if __name__ == "__main__":
    main()
