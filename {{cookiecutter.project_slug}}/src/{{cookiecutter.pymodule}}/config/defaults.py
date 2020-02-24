from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

__all__ = [
    "DEFAULT_CONFIG_FILE",
    "DEFAULT_CONFIG_FILE_ENV_VAR",
    "DEFAULT_WEB_CONFIG",
]

DEFAULT_CONFIG_FILE_ENV_VAR = "{{ cookiecutter.pymodule.upper() }}_CONFIG_FILE"
DEFAULT_CONFIG_FILE = "/etc/{{ cookiecutter.project_slug }}.yaml"

DEFAULT_WEB_CONFIG = {
    "swagger_ui": True,
    "serve_spec": True,
    "port": {{ cookiecutter.default_port }},
    "host": "127.0.0.1",
}
