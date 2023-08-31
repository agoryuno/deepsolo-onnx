from typing import Union
from pathlib import Path
from detectron2.config import CfgNode, get_cfg


def load_config(yaml_path: Union[str, Path]) -> 'CfgNode':
    """
    Load and register the configuration settings for the ViTAE_V2 model from a YAML file and return a Detectron2 CfgNode.

    Parameters:
        yaml_path (Union[str, Path]): The path to the YAML configuration file.

    Returns:
        CfgNode: A Detectron2 CfgNode object containing the loaded and registered configuration settings.
    """

    cfg = get_cfg()

    # Register custom fields
    cfg.MODEL.ViTAEv2 = get_cfg().new()
    cfg.MODEL.TRANSFORMER = get_cfg().new()
    cfg.MODEL.TRANSFORMER.LOSS = get_cfg().new()
    cfg.SOLVER = get_cfg().new()
    cfg.SOLVER.CLIP_GRADIENTS = get_cfg().new()
    cfg.INPUT = get_cfg().new()
    cfg.INPUT.CROP = get_cfg().new()
    cfg.DATALOADER = get_cfg().new()

    # Merge the YAML config
    cfg.merge_from_file(yaml_path)
    return cfg

