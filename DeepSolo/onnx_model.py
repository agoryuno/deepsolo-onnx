from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
from vitae_v2 import ViTAEv2

class SimpleONNXReadyModel:
    def __init__(self, config_file):
        self.cfg = get_cfg()
        self.cfg.merge_from_file(config_file)
        self.cfg.freeze()
        self.predictor = DefaultPredictor(self.cfg)
        
    def forward(self, image):
        return self.predictor(image)
