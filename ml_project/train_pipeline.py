"""Train pipeline module"""
import sys
import logging

import click


from entities import (
    read_training_pipeline_params
)

from data import (
    read_data,
    split_train_val_data,
    save_object
)

from features import (
    extract_target,
    build_transformer,
    make_features
)

from models import (
    train_model,
    create_inference_pipeline,
    predict_model,
    evaluate_model
)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s"
)
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def run_train_pipeline(training_pipeline_params):
    """Runs train pipeline"""
    logger.info(
        "start train pipeline with params: %s",
        training_pipeline_params
    )
    data = read_data(training_pipeline_params.input_data_path)
    logger.info("data shape: %s", data.shape)
    train_df, val_df = split_train_val_data(
        data, training_pipeline_params.splitting_params
    )

    train_target = extract_target(
        train_df,
        training_pipeline_params.feature_params
    )
    train_df = train_df.drop(
        training_pipeline_params.feature_params.target_col,
        1
    )
    logger.info("train data shape: %s", train_df.shape)

    val_target = extract_target(
        val_df,
        training_pipeline_params.feature_params
    )
    val_df = val_df.drop(training_pipeline_params.feature_params.target_col, 1)
    logger.info("validation data shape: %s", val_df.shape)

    if training_pipeline_params.use_transformers:
        transformer = build_transformer(training_pipeline_params)
        transformer.fit(train_df)
    else:
        transformer = None

    train_features = make_features(transformer, train_df)
    logger.info("train_features.shape is %s", train_features.shape)
    model = train_model(
        train_features, train_target, training_pipeline_params.train_params
    )

    inference_pipeline = create_inference_pipeline(model, transformer)
    predicts = predict_model(
        inference_pipeline,
        val_df
    )
    metrics = evaluate_model(
        predicts,
        val_target
    )

    save_object(metrics, training_pipeline_params.metric_path, save_as="json")

    model_path = training_pipeline_params.output_model_path
    save_object(inference_pipeline, model_path)

    return model_path, metrics


@click.command(name="train_pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    """Train pipeline entry point"""
    # train_pipeline(config_path)
    training_pipeline_params = read_training_pipeline_params(config_path)
    run_train_pipeline(training_pipeline_params)


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter
    train_pipeline_command()
