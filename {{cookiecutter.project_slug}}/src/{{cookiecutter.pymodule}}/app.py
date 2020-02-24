from __future__ import annotations

import asyncio
import logging
import os

import connexion
import uvloop

from . import di
from .config import build_config_loader

logger = logging.getLogger(__name__)

__all__ = ["main"]


def prepare_web_controllers(options: dict) -> connexion.AioHttpApp:
    specification_dir = os.path.join(os.path.dirname(__file__), "openapi")
    app = connexion.AioHttpApp(
        __name__,
        specification_dir=specification_dir,
        options=options,
        only_one_api=True,
    )
    app.add_api(
        "openapi.yaml",
        arguments={"title": "{{ cookiecutter.project_name }}"},
        pythonic_params=True,
        pass_context_arg_name="request",
    )
    return app


def main():
    # use uvloop (it's faster!) with aiohttp (via asyncio).
    #   https://github.com/MagicStack/uvloop/issues/13
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    root_config = build_config_loader().load()
    di.container.register("config", lambda: root_config.copy())

    web_options: dict = root_config["web"]
    # web_options["middlewares"] = [@aiohttp.web.middleware]
    # web_options["access_log"] = logging.Logger instance
    port = web_options.pop("port")
    host = web_options.pop("host")
    app = prepare_web_controllers(web_options)
    app.run(port=port, host=host)
