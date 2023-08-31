from typing import Union
from pathlib import Path
from detectron2.config import CfgNode, get_cfg


def load_config(yaml_path: Union[str, Path]) -> 'CfgNode':
    """
    Load and register the configuration settings.
    """
    template_cfg = CfgNode.load_yaml_with_base(yaml_path)
    cfg = get_cfg()

    for key, value in template_cfg.items():
        if key not in cfg:
            if isinstance(value, dict):
                cfg[key] = CfgNode(value)
            else:
                cfg[key] = value

    # Now that keys are registered, merge the YAML
    cfg.merge_from_file(yaml_path)
    return cfg

def load_config2(yaml_path: Union[str, Path]) -> 'CfgNode':
    """
    Load and register the configuration settings for the ViTAE_V2 model from a YAML file and return a Detectron2 CfgNode.

    Parameters:
        yaml_path (Union[str, Path]): The path to the YAML configuration file.

    Returns:
        CfgNode: A Detectron2 CfgNode object containing the loaded and registered configuration settings.
    """

    cfg = get_cfg()

    # Register custom fields
    cfg.MODEL.ViTAEv2 = CfgNode()
    cfg.MODEL.ViTAEv2.TYPE = ""
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

