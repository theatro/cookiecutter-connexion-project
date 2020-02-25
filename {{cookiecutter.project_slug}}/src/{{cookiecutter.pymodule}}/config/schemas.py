# NOTE: Do not use __future__ annotations on marshmallow model files

import logging

from cfg_loader import ConfigSchema
from marshmallow import fields

from .defaults import DEFAULT_WEB_CONFIG

logger = logging.getLogger(__name__)

__all__ = ["AppOptions"]


class WebOptions(ConfigSchema):

    # connexion.options.ConnexionOptions
    swagger_ui = fields.Boolean(
        default=DEFAULT_WEB_CONFIG["swagger_ui"],
        missing=DEFAULT_WEB_CONFIG["swagger_ui"],
    )  # openapi_console_ui_available
    # swagger_url = fields.String(default="/ui")  # openapi_console_ui_path
    # swagger_path = fields.String()  # openapi_spec_ui_from_dir
    serve_spec = fields.Boolean(
        default=DEFAULT_WEB_CONFIG["serve_spec"],
        missing=DEFAULT_WEB_CONFIG["serve_spec"],
    )  # openapi_spec_available
    # openapi_spec_path = fields.String(default="/openapi.json")  # openapi_spec_path
    # uri_parser_class = enum(
    #     OpenAPIURIParser, Swagger2URIParser, FirstValueURIParser, AlwaysMultiURIParser
    # )

    # connexion.apps.AioHttpApp options
    # access_log = Optional[logging.Logger] class co change access_log formatting
    use_default_access_log = fields.Boolean(default=False)

    # connexion.apis.AioHttpApi options
    # middlewares = list of @web.middleware coroutines that get added after defaults
    #   default middlewares = [
    #       oauth_problem_middleware, <- some fixes included after 2.2.0
    #       trailing_slash_redirect  <- added after 2.2.0
    #   ]

    # connexion.apps.AioHttpApp.run() options
    port = fields.Integer(
        default=DEFAULT_WEB_CONFIG["port"], missing=DEFAULT_WEB_CONFIG["port"]
    )
    host = fields.String(
        default=DEFAULT_WEB_CONFIG["host"], missing=DEFAULT_WEB_CONFIG["host"]
    )


class AppOptions(ConfigSchema):
    web = fields.Nested(WebOptions, missing=DEFAULT_WEB_CONFIG)
