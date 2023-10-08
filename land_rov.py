#!/usr/bin/env python3
"""
Polyglot v3 node server Lighting Version
Copyright (C) 2023 by Steven Bailey
"""
import logging
import jlrpy
from nodes import JaguarController
from nodes import JaguarNode
import udi_interface
import sys

LOGGER = udi_interface.LOGGER
LOG_HANDLER = udi_interface.LOG_HANDLER


if __name__ == "__main__":
    try:
        LOGGER.debug("Staring Jaguar Interface")
        polyglot = udi_interface.Interface([JaguarController, JaguarNode])
        polyglot.start()
        control = JaguarController(polyglot, 'controller', 'controller', 'Jaguar Land Rover')
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        polyglot.stop()
        sys.exit(0)
    except Exception as err:
        LOGGER.error('Exception: {0}'.format(err), exc_info=True)
        sys.exit(0)
