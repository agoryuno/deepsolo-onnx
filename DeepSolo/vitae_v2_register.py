from typing import Union
from pathlib import Path
from detectron2.config import CfgNode
from .defaults import _C


def load_config(yaml_path: Union[str, Path]) -> 'CfgNode':
    """
    Load and register the configuration settings for the ViTAE_V2 model from a YAML file and return a Detectron2 CfgNode.

    Parameters:
        yaml_path (Union[str, Path]): The path to the YAML configuration file.

    Returns:
        CfgNode: A Detectron2 CfgNode object containing the loaded and registered configuration settings.
    """

    # Merge the YAML config
    _C.merge_from_file(yaml_path)
    return _C

