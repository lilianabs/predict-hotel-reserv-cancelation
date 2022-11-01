from steps.load_data import load_training_data
from steps.clean_data import clean_data
from steps.split_train_data import split_train_data
from steps.train_model import train_model
from steps.evaluate_model import evaluate_model
from steps.evaluate_deployment import evaluate_deployment
from steps.deploy_model import deploy_model
from steps.load_data import load_inference_data
from steps.prediction_steps import prediction_service_loader
from steps.prediction_steps import predictor
from steps.drift_detection import drift_detector
from pipelines.training_pipeline import training_pipeline
from pipelines.inference_pipeline import batch_inference_pipeline

from zenml.integrations.evidently.visualizers import EvidentlyVisualizer


def inference_run():
    """Runs inference pipeline
    """

    inference_pipeline_instance = inference_pipeline(
        load_inference_data=load_inference_data(),
        prediction_service_loader=prediction_service_loader(),
        predictor=predictor(),
        load_training_data=load_training_data(),
        drift_detector=drift_detector,
    )

    inference_pipeline_instance.run()

    inf_run = inference_pipeline_instance.get_runs()[-1]
    drift_detection_step = inf_run.get_step(step="drift_detector")
    EvidentlyVisualizer().visualize(drift_detection_step)


# if __name__ == "__main__":
# inference_run()
