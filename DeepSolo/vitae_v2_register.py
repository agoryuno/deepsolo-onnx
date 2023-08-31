from typing import Union
from os import Path
from detectron2.config import CfgNode


def load_config(yaml_path: Union[str, Path]) -> 'CfgNode':
    """
    Load and register the configuration settings for the ViTAE_V2 model from a YAML file and return a Detectron2 CfgNode.

    Parameters:
        yaml_path (Union[str, Path]): The path to the YAML configuration file.

    Returns:
        CfgNode: A Detectron2 CfgNode object containing the loaded and registered configuration settings.
    """

    cfg = CfgNode(new_allowed=True)

    # Register custom fields
    cfg.MODEL.ViTAEv2 = CfgNode()
    cfg.MODEL.TRANSFORMER = CfgNode()
    cfg.MODEL.TRANSFORMER.LOSS = CfgNode()
    cfg.SOLVER = CfgNode()
    cfg.SOLVER.CLIP_GRADIENTS = CfgNode()
    cfg.INPUT = CfgNode()
    cfg.INPUT.CROP = CfgNode()
    cfg.DATALOADER = CfgNode()

    # Merge the YAML config
    cfg.merge_from_file(yaml_path)
    return cfg

