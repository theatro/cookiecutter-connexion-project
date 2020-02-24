# NOTE: Do not use __future__ annotations on marshmallow model files

import logging

from marshmallow import Schema, RAISE, post_load, post_dump

logger = logging.getLogger(__name__)


class SchemaBase(Schema):
    @property
    def __model__(self):
        raise NotImplementedError

    class Meta:
        # Server models should not tolerate random fields from the client. The Zalando specs do a good job of explaining
        # why this is important in API extensibility: https://opensource.zalando.com/restful-api-guidelines/#109
        # So, tell marshmallow to raise ValidationErrors for unknown fields.
        # https://marshmallow.readthedocs.io/en/3.0/quickstart.html#handling-unknown-fields
        unknown = RAISE

    @post_load
    def make_object__(self, data):
        return self.__model__(**data)

    # validation occurs on load, not on dump. This works well server-side where we're loading requests or loading data.
    # client-side will need to validate on serialize so that they can error before making a request.
