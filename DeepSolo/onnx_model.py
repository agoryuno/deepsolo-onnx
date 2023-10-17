from typing import Union
from pathlib import Path

import torch
from torch import nn
import numpy as np

from detectron2.modeling import build_model
#from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
import detectron2.data.transforms as T
from detectron2.checkpoint import DetectionCheckpointer

from .adet.config import get_cfg
from .adet.data.augmentation import Pad
from .adet.modeling.vitae_v2.vitae_v2 import ViTAEv2


def setup_cfg(config_path: Union[str, Path], weights_path: str):
    cfg = get_cfg()
    cfg.merge_from_file(config_path)
    weights = ["MODEL.WEIGHTS", weights_path]
    cfg.merge_from_list(weights)
    cfg.freeze()
    return cfg


def SimpleONNXReadyModel(config_path, weights_path):
    cfg = setup_cfg(config_path, weights_path)
    cfg.freeze()
    return ViTAEPredictor(cfg)
        

class ViTAEPredictor(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg.clone()

        # `self.cfg` contains a setting `META.MODEL_ARCHITECTUR`
        # which is set to `TransformerPureDetector` 
        # `build_model()` uses that setting to instantiate 
        # `adet.modelling.text_spotter.TransformerPureDetector` as
        # the underlying model. `TransformerPureDetector` is a `torch.nn.Module`
        # that performs the actual work
        self.model = build_model(self.cfg)
        self.model.eval()

        checkpointer = DetectionCheckpointer(self.model)
        checkpointer.load(cfg.MODEL.WEIGHTS)

        self.aug = T.ResizeShortestEdge(
            [cfg.INPUT.MIN_SIZE_TEST, cfg.INPUT.MIN_SIZE_TEST], cfg.INPUT.MAX_SIZE_TEST
        )
        # each dim must be divisible by 32 with no remainder for ViTAE
        self.pad = Pad(divisible_size=32)

        self.input_format = cfg.INPUT.FORMAT
        assert self.input_format in ["RGB", "BGR"], self.input_format

    def forward(self, original_image):
        """
        Args:
            original_image (np.ndarray): an image of shape (H, W, C) (in BGR order).

        Returns:
            predictions (dict):
                the output of the model for one image only.
        """
        original_image = original_image[0]
        with torch.no_grad():  # https://github.com/sphinx-doc/sphinx/issues/4258
            if self.input_format == "RGB":
                #original_image = original_image[:, :, ::-1]
                original_image = torch.flip(original_image, [-1])
            height, width = original_image.shape[:2]
            height = height.item()
            width = width.item()
            #image = self.aug.get_transform(original_image).apply_image(original_image)
            #image = self.pad.get_transform(image).apply_image(image)
            #image = torch.as_tensor(image.astype("float32").transpose(2, 0, 1))
            image = original_image.to(torch.float32)
            inputs = {"image": image, "height": height, "width": width}
            predictions = self.model([inputs])
            return predictions