"""
Polyglot PG3x node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 1.0.0 Jun 2023
"""

import udi_interface
import jlrpy
import logging
import time
from nodes import JaguarNode

LOGGER = udi_interface.LOGGER
LOG_HANDLER = udi_interface.LOG_HANDLER
Custom = udi_interface.Custom
ISY = udi_interface.ISY

# IF you want a different log format than the current default
LOG_HANDLER.set_log_format('%(asctime)s %(threadName)-10s %(name)-18s %(levelname)-8s %(module)s:%(funcName)s: %(message)s')

class JaguarController(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name):
        super(JaguarController, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.hb = 0
        self.name = self.got['vehicleBrand']  # override what was passed in
        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')
        self.TypedParameters = Custom(polyglot, 'customtypedparams')
        self.TypedData = Custom(polyglot, 'customtypeddata')
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.LOGLEVEL, self.handleLevelChange)
        self.poly.subscribe(self.poly.CUSTOMPARAMS, self.parameterHandler)
        self.poly.subscribe(self.poly.CUSTOMTYPEDPARAMS, self.typedParameterHandler)
        self.poly.subscribe(self.poly.CUSTOMTYPEDDATA, self.typedDataHandler)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.poly.ready()
        self.poly.addNode(self)

    def start(self):
        self.poly.updateProfile()
        self.poly.setCustomParamsDoc()
        self.heartbeat(0)
        self.discover()
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        self.got = v.get_attributes()
        

    def parameterHandler(self, params):
        self.Parameters.load(params)
        LOGGER.debug('Loading parameters now')
        self.check_params()

    def typedParameterHandler(self, params):
        self.TypedParameters.load(params)
        LOGGER.debug('Loading typed parameters now')
        LOGGER.debug(params)

    def typedDataHandler(self, params):
        self.TypedData.load(params)
        LOGGER.debug('Loading typed data now')
        LOGGER.debug(params)

    def handleLevelChange(self, level):
        LOGGER.info('New log level: {}'.format(level))

    def poll(self, flag):
        if 'longPoll' in flag:
            LOGGER.debug('longPoll (controller)')
            self.heartbeat()
        else:
            LOGGER.debug('shortPoll (controller)')

    def query(self,command=None):
        nodes = self.poly.getNodes()
        for node in nodes:
            nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        got = v.get_attributes()
        LOGGER.info(got['nickname'])
        LOGGER.info(got['modelYear'])
        LOGGER.info(got['vehicleBrand'])
        LOGGER.info(got['vehicleType'])
        self.poly.addNode(JaguarNode(self.poly, self.address, 'jaguaraddr', got['nickname'], self.email, self.password, self.pin))

    def stop(self):
        LOGGER.debug('NodeServer stopped.')

    def heartbeat(self,init=False):
        LOGGER.debug('heartbeat: init={}'.format(init))
        if init is not False:
            self.hb = init
        LOGGER.debug('heartbeat: hb={}'.format(self.hb))
        if self.hb == 0:
            self.reportCmd("DON",2)
            self.hb = 1
        else:
            self.reportCmd("DOF",2)
            self.hb = 0

    def set_module_logs(self,level):
        logging.getLogger('urllib3').setLevel(level)

    def check_params(self):
        self.Notices.clear()
        default_email = "joe@ddd.net"
        default_password = "go with your password"
        default_pin = "1234"

        self.email = self.Parameters.email
        if self.email is None:
            self.email = default_email
            LOGGER.error('check_params: email not defined in customParams, please add it.  Using {}'.format(default_email))
            self.email = default_email

        self.password = self.Parameters.password
        if self.password is None:
            self.password = default_password
            LOGGER.error('check_params: password not defined in customParams, please add it.  Using {}'.format(default_password))
            self.password = default_password
            
        self.pin = self.Parameters.pin
        if self.pin is None:
            self.pin = default_pin
            LOGGER.error('check_params: pin not defined in customParams, please add it.  Using {}'.format(default_password))
            self.pin = default_pin

        # Add a notice if they need to change the email/password from the default.
        if self.email == default_email or self.password == default_password or self.pin == default_pin:
            self.Notices['auth'] = 'Please set proper email and password and pin in the configuration page then restart'
            self.Notices['test'] = 'Jaguar, Land Rover'


    def remove_notice_test(self,command):
        LOGGER.info('remove_notice_test: notices={}'.format(self.Notices))
        self.Notices.delete('test')

    def remove_notices_all(self,command):
        LOGGER.info('remove_notices_all: notices={}'.format(self.Notices))
        self.Notices.clear()

    id = 'landctrl'
    commands = {
        #'QUERY': query,
        'REMOVE_NOTICES_ALL': remove_notices_all,
        'REMOVE_NOTICE_TEST': remove_notice_test,
    }
    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2, 'name': "Online"},
    ]
