#!/usr/bin/env python3.7
from __future__ import annotations

import logging

from .app import main

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # TODO: pycharm remote debugging support based on env var
    main()
