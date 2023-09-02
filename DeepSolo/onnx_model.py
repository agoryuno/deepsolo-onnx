from typing import Union
from pathlib import Path

import torch

from detectron2.modeling import build_model
from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
import detectron2.data.transforms as T
from detectron2.checkpoint import DetectionCheckpointer

from .adet.data.augmentation import Pad
from .adet.modeling.vitae_v2.vitae_v2 import ViTAEv2



def setup_cfg(config_file: Union[str, Path]):
    cfg = get_cfg()
    cfg.merge_from_file(config_file)
    cfg.freeze()
    return cfg


class SimpleONNXReadyModel:
    def __init__(self, config_path):
        self.cfg = setup_cfg(config_path)
        self.cfg.freeze()
        self.predictor = DefaultPredictor(self.cfg)
        
    def forward(self, image):
        return self.predictor(image)
    

class ViTAEPredictor:
    def __init__(self, cfg):
        self.cfg = cfg.clone()
        self.model = build_model(self.cfg)
        self.model.eval()

        checkpointer = DetectionCheckpointer(self.model)
        checkpointer.load(cfg.MODEL.WEIGHTS)

        self.aug = T.ResizeShortestEdge(
            [cfg.INPUT.MIN_SIZE_TEST, cfg.INPUT.MIN_SIZE_TEST], cfg.INPUT.MAX_SIZE_TEST
        )
        # each size must be divided by 32 with no remainder for ViTAE
        self.pad = Pad(divisible_size=32)

        self.input_format = cfg.INPUT.FORMAT
        assert self.input_format in ["RGB", "BGR"], self.input_format

    def __call__(self, original_image):
        """
        Args:
            original_image (np.ndarray): an image of shape (H, W, C) (in BGR order).

        Returns:
            predictions (dict):
                the output of the model for one image only.
                See :doc:`/tutorials/models` for details about the format.
        """
        with torch.no_grad():  # https://github.com/sphinx-doc/sphinx/issues/4258
            if self.input_format == "RGB":
                original_image = original_image[:, :, ::-1]
            height, width = original_image.shape[:2]
            image = self.aug.get_transform(original_image).apply_image(original_image)
            image = self.pad.get_transform(image).apply_image(image)
            image = torch.as_tensor(image.astype("float32").transpose(2, 0, 1))
            inputs = {"image": image, "height": height, "width": width}
            predictions = self.model([inputs])[0]
            return predictions
