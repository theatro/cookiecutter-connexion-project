import logging

import inflection

from connexion.operations import AbstractOperation
from connexion.resolver import RestyResolver

logger = logging.getLogger(__name__)

__all__ = ["SpecTagsResolver"]


class SpecTagsResolver(RestyResolver):
    """
    Resolves endpoint functions using controller names derived from tags in the spec.

    base_controller_module.tag_controller.operation_id

    If the spec does not define an operationId, then RestyResolver will provide one:

    base_controllers_module.tag_controller.path_based_resource.method
    base_controllers_module.path_based_resource.method (no tag)

    If the spec defines x-openapi-controller-name, that takes precedence:

    x_openapi_controller.operation_id
    x_openapi_controller.path_based_resource.method (no operationId)
    """

    def __init__(
        self,
        base_controllers_module: str,
        default_module_name: str = "default_controller",
        collection_endpoint_name: str = "search",
    ):
        self.base_controllers_module = base_controllers_module
        super(SpecTagsResolver, self).__init__(
            self._fq_controller(default_module_name), collection_endpoint_name
        )

    def _fq_controller(self, controller_name):
        return "{}.{}".format(self.base_controllers_module, controller_name)

    def resolve_operation_id(self, operation: AbstractOperation) -> str:
        """
        Resolves the controller
        """
        operation_id = operation.operation_id
        has_simple_operation_id = operation_id and "." not in operation_id
        has_fq_operation_id = operation_id and "." in operation_id

        if has_simple_operation_id:
            operation._operation_id = inflection.underscore(operation_id)
        if not operation.router_controller and not has_fq_operation_id:
            # noinspection PyProtectedMember
            spec: dict = operation._operation
            tags: list = spec.get("tags", [])
            if tags:
                # TODO: underscore that matches how openapi-generator does
                #       camelize(underscore(tag))
                tag = inflection.underscore(tags[0]).replace(" ", "_")
                controller_name = tag + "_controller"
                operation._router_controller = self._fq_controller(controller_name)

        return super(SpecTagsResolver, self).resolve_operation_id(operation)
