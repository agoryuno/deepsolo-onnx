from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
from .vitae_v2 import ViTAEv2
from .vitae_v2_register import load_config

class SimpleONNXReadyModel:
    def __init__(self, config_path):
        self.cfg = load_config(config_path)
        self.cfg.freeze()
        self.predictor = DefaultPredictor(self.cfg)
        
    def forward(self, image):
        return self.predictor(image)
