from __future__ import annotations

import logging

from connexion.exceptions import ProblemException

logger = logging.getLogger(__name__)


class AppProblem(ProblemException):
    """The base Problem for all exceptions created by this App"""
