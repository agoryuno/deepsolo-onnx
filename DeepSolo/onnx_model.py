from typing import Union
from pathlib import Path

from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
from .adet.modeling.vitae_v2.vitae_v2 import ViTAEv2

#from .vitae_v2 import ViTAEv2
#from .vitae_v2_register import load_config


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
