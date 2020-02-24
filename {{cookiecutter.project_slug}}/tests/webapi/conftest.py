import logging
import pytest
import os

import connexion

from {{ cookiecutter.pymodule }} import di
from {{ cookiecutter.pymodule }}.web.resolver import SpecTagsResolver


@pytest.fixture
def base_test_config():
    return {
        "web": {
            "swagger_ui": True,
            "serve_spec": True,
            # "middlewares": [@aiohttp.web.middleware],
        },
    }


@pytest.fixture
def client(loop, aiohttp_client, base_test_config):
    logging.getLogger("connexion.operation").setLevel("ERROR")
    options = base_test_config["web"]
    specification_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "src", "{{ cookiecutter.pymodule }}", "openapi"
    )
    app = connexion.AioHttpApp(
        __name__,
        specification_dir=specification_dir,
        options=options,
        only_one_api=True,
    )
    resolver = SpecTagsResolver(
        "{{ cookiecutter.pymodule }}.web.controllers", default_module_name="default_controller"
    )
    app.add_api(
        "openapi.yaml",
        pythonic_params=True,
        pass_context_arg_name="request",
        resolver=resolver,
    )
    app_client = aiohttp_client(app.app)
    return loop.run_until_complete(app_client)


@pytest.fixture
def container(base_test_config):
    di.container.register("config", lambda: base_test_config.copy())
    # inject things here (such as persistence queries)
    return di.container
