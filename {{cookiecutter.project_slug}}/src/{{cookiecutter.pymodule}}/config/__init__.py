from __future__ import annotations

import logging
import os

from cfg_loader import YamlConfigLoader
from .schemas import AppOptions
from .defaults import DEFAULT_CONFIG_FILE, DEFAULT_CONFIG_FILE_ENV_VAR

logger = logging.getLogger(__name__)

__all__ = [
    "DEFAULT_CONFIG_FILE",
    "DEFAULT_CONFIG_FILE_ENV_VAR",
    "AppOptions",
    "build_config_loader",
]


def build_config_loader(
    config_file_env_var=DEFAULT_CONFIG_FILE_ENV_VAR,
    default_config_path=DEFAULT_CONFIG_FILE,
    substitution_mapping=os.environ,
    **kwargs,
) -> YamlConfigLoader:
    return YamlConfigLoader(
        AppOptions,
        config_file_env_var=config_file_env_var,
        default_config_path=default_config_path,
        substitution_mapping=substitution_mapping,
        **kwargs,
    )
