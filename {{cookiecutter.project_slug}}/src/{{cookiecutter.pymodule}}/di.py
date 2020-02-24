from __future__ import annotations

import logging

import punq

logger = logging.getLogger(__name__)

__all__ = ["container"]


# see https://io.made.com/dependency-injection-with-type-signatures-in-python/
container = punq.Container()
