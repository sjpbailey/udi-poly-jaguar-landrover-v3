"""
Polyglot PG3x node server
Copyright (C) 2023 Steven Bailey
MIT License
Version 1.0.0 Jun 2023
"""
import udi_interface
import Examples.jlrpy as jlrpy
import logging
import sys
import time
import urllib3

LOGGER = udi_interface.LOGGER


class JaguarNode(udi_interface.Node):

    def __init__(self, polyglot, primary, address, name, email, password, pin):
        super(JaguarNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)

        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)

        self.email = email
        self.password = password
        self.pin = pin

    def start(self):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        # self.goNow(self)
        go = v.get_status()

        # Climate
        self.setDriver('GV19', v.get_status(
            "CLIMATE_STATUS_REMAINING_RUNTIME"))
        tempestpt = v.get_status("CLIMATE_STATUS_REMAINING_RUNTIME")
        LOGGER.info(f"CLIMATE REMAINING RUNTIME = {tempestpt} minutes\n")

        # Vehicle State
        vehstate = v.get_status("VEHICLE_STATE_TYPE")
        LOGGER.info(f"CURRENT VEHICLE STATE = {vehstate} \n")
        if v.get_status("VEHICLE_STATE_TYPE") == "ENGINE_ON_REMOTE_START":
            self.setDriver('GV20', 1)
        else:
            self.setDriver('GV20', 0)

        # VARIABLES
        self.setDriver('GV1', v.get_status("ODOMETER_MILES"))
        LOGGER.info("ODOMETER_MILES")
        LOGGER.info(v.get_status("ODOMETER_MILES"))
        self.setDriver('GV21', v.get_status("ODOMETER_METER"))
        LOGGER.info("ODOMETER_METER")
        LOGGER.info(v.get_status("ODOMETER_METER"))
        if v.get_status("ODOMETER_MILES") is not None:
            self.setDriver('ST', 1)
        else:
            self.setDriver('ST', 0)
        self.setDriver('GV2', v.get_status("BATTERY_VOLTAGE"))
        self.setDriver('GV13', round(
            float(v.get_status("TYRE_PRESSURE_FRONT_RIGHT"))*.01))
        self.setDriver('GV14', round(
            float(v.get_status("TYRE_PRESSURE_FRONT_LEFT"))*.01))
        self.setDriver('GV15', round(
            float(v.get_status("TYRE_PRESSURE_REAR_RIGHT"))*.01))
        self.setDriver('GV16', round(
            float(v.get_status("TYRE_PRESSURE_REAR_LEFT"))*.01))

        # WARNINGS
        LOGGER.info("OIL_LEVEL_WARN")
        LOGGER.info(v.get_status("EXT_OIL_LEVEL_WARN"))
        if v.get_status("EXT_OIL_LEVEL_WARN") == "NORMAL":
            self.setDriver('GV3', 0)
        else:
            self.setDriver('GV3', 1)
        LOGGER.info("COOLANT_TEMP")
        LOGGER.info(v.get_status("ENGINE_COOLANT_TEMP"))
        self.setDriver('GV4', v.get_status("ENGINE_COOLANT_TEMP"))
        LOGGER.info("COOLANT_LEVEL_WARN")
        LOGGER.info(v.get_status("ENG_COOLANT_LEVEL_WARN"))
        if v.get_status("ENG_COOLANT_LEVEL_WARN") == "NORMAL":
            self.setDriver('GV5', 0)
        else:
            self.setDriver('GV5', 1)
        LOGGER.info("BRAKE_FLUID_WARN")
        LOGGER.info(v.get_status("BRAKE_FLUID_WARN"))
        if v.get_status("BRAKE_FLUID_WARN") == "NORMAL":
            self.setDriver('GV6', 0)
        if v.get_status("BRAKE_FLUID_WARN") == "ALARM":
            self.setDriver('GV6', 1)
        LOGGER.info("WASHER_FLUID_WARN")
        LOGGER.info(v.get_status("WASHER_FLUID_WARN"))
        if v.get_status("WASHER_FLUID_WARN") == "NORMAL":
            self.setDriver('GV7', 0)
        if v.get_status("WASHER_FLUID_WARN") == "ALARM":
            self.setDriver('GV7', 1)

        # DOORS
        LOGGER.info("DOOR_FRONT_LEFT_LOCK_STATUS")
        LOGGER.info(v.get_status("DOOR_FRONT_LEFT_LOCK_STATUS"))

        LOGGER.info("DOOR_FRONT_RIGHT_LOCK_STATUS")
        LOGGER.info(v.get_status("DOOR_FRONT_RIGHT_LOCK_STATUS"))

        LOGGER.info("DOOR_REAR_LEFT_LOCK_STATUS")
        LOGGER.info(v.get_status("DOOR_REAR_LEFT_LOCK_STATUS"))

        LOGGER.info("DOOR_REAR_RIGHT_LOCK_STATUS")
        LOGGER.info(v.get_status("DOOR_REAR_RIGHT_LOCK_STATUS"))

        LOGGER.info("DOOR_IS_ALL_DOORS_LOCKED")
        LOGGER.info(v.get_status("DOOR_IS_ALL_DOORS_LOCKED"))

        # DOOR LOCKS
        LOGGER.info("THEFT_ALARM_STATUS")
        LOGGER.info(v.get_status("THEFT_ALARM_STATUS"))
        if v.get_status("THEFT_ALARM_STATUS") == "ALARM_ARMED":
            self.setDriver('GV22', 1)
        else:
            self.setDriver('GV22', 0)

        if v.get_status("DOOR_IS_ALL_DOORS_LOCKED") == "TRUE":
            self.setDriver('GV8', 1)
            LOGGER.info('LOCKED')
        else:
            self.setDriver('GV8', 0)
            LOGGER.info('UNLOCKED')
        LOGGER.info("DOOR_ENGINE_HOOD_LOCK_STATUS")
        LOGGER.info(v.get_status("DOOR_ENGINE_HOOD_LOCK_STATUS"))
        if v.get_status("DOOR_ENGINE_HOOD_LOCK_STATUS") == "LOCKED":
            self.setDriver('GV11', 1)
            LOGGER.info('HOOD LOCKED')
        else:
            self.setDriver('GV11', 0)
            LOGGER.info('HOOD UNLOCKED')
        LOGGER.info("DOOR_IS_BOOT_LOCKED")
        LOGGER.info(v.get_status("DOOR_IS_BOOT_LOCKED"))
        if v.get_status("DOOR_IS_BOOT_LOCKED") == "TRUE":
            self.setDriver('GV12', 1)
            LOGGER.info('BOOT LOCKED')
        else:
            self.setDriver('GV12', 0)
            LOGGER.info('BOOT UNLOCKED')
        LOGGER.info("DOOR_IS_BOOT_LOCKED")
        LOGGER.info(v.get_status("DOOR_IS_BOOT_LOCKED"))
        if v.get_status("IS_SUNROOF_OPEN") == "TRUE":
            self.setDriver('GV17', 1)
            LOGGER.info('SUNROOF OPEN')
        else:
            self.setDriver('GV17', 0)
            LOGGER.info('SUNROOF CLOSED')

    def lckunlck(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        door = int(float(command.get('value')))
        if door == 1:
            v.lock(self.pin)
            self.setDriver('GV10', 0)
            time.sleep(5)
            self.reportDrivers()
        elif door == 0:
            v.unlock(self.pin)
            self.setDriver('GV10', 1)
            time.sleep(5)
            self.reportDrivers()
        else:
            logging.error('Unknown command for Lock Doors {}'.format(command))

    def privacy(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        mode = int(float(command.get('value')))
        if mode == 1:
            v.enable_privacy_mode(self.pin)
            self.setDriver('GV23', 0)
            time.sleep(5)
            self.reportDrivers()
        elif mode == 0:
            v.disable_privacy_mode(self.pin)
            self.setDriver('GV23', 1)
            time.sleep(5)
            self.reportDrivers()
        else:
            logging.error(
                'Unknown command for Privacy Mode {}'.format(command))

    def beep(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        v.honk_blink()
        v.reset_alarm(self.pin)

    def alrmreset(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        v.reset_alarm(self.pin)

    def dim(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        temptur = float(command.get('value'))
        self.setDriver('GV18', temptur)
        LOGGER.info(temptur)
        # convert to celsius
        temptur = round(int((temptur - 32) * 5.0/9.0))*10
        LOGGER.info(f"Setpoint = {temptur}\n")
        v.preconditioning_start(temptur)
        temptur = (temptur)/10
        LOGGER.info(f"RCC Setpoint = {temptur}\n")
        v.set_rcc_target_value(self.pin, (temptur))
        v.remote_engine_start(self.pin, temptur)
        LOGGER.info("Starting")
        time.sleep(9)
        self.start()

    def strt(self, command):
        temptur = self.temptur
        self.dim()
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        v.remote_engine_start(self.pin, temptur)
        time.sleep(1)
        LOGGER.info("Start")

    def stp(self, command):
        c = jlrpy.Connection(self.email, self.password)
        v = c.vehicles[0]
        v.remote_engine_stop(self.pin)
        v.preconditioning_stop()
        time.sleep(9)
        self.start()

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            LOGGER.debug('shortPoll (node)')
            self.reportDrivers()
            self.start()
            # nodes = self.poly.getNodes()

    def query(self, command=None):
        # self.reportDrivers()
        self.start()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2, 'name': "Online"},
        {'driver': 'GV1', 'value': 0, 'uom': 116, 'name': 'Milage'},
        {'driver': 'GV2', 'value': 0, 'uom': 72, 'name': 'Battery Voltage'},
        {'driver': 'GV3', 'value': 0, 'uom': 25, 'name': 'Oil Level Warning'},
        {'driver': 'GV4', 'value': 0, 'uom': 17, 'name': 'Coolant Temp'},
        {'driver': 'GV5', 'value': 0, 'uom': 25, 'name': 'Cool Level Warning'},
        {'driver': 'GV6', 'value': 0, 'uom': 25, 'name': 'Brake Fluid Warning'},
        {'driver': 'GV7', 'value': 0, 'uom': 25, 'name': 'Washer Fluid Warning'},
        {'driver': 'GV8', 'value': 0, 'uom': 25, 'name': 'Doors Locked'},
        {'driver': 'GV10', 'value': 0, 'uom': 25, 'name': 'Door Lock Unlock'},
        {'driver': 'GV11', 'value': 0, 'uom': 25, 'name': 'Hood Lock Unlock'},
        {'driver': 'GV12', 'value': 0, 'uom': 25, 'name': 'Boot Lock Unlock'},
        {'driver': 'GV13', 'value': 0, 'uom': 56, 'name': 'Front R Tire'},
        {'driver': 'GV14', 'value': 0, 'uom': 56, 'name': 'Front L Tire'},
        {'driver': 'GV15', 'value': 0, 'uom': 56, 'name': 'Rear R Tire'},
        {'driver': 'GV16', 'value': 0, 'uom': 56, 'name': 'Rear L Tire'},
        {'driver': 'GV17', 'value': 0, 'uom': 25, 'name': 'Sun Roof Open'},
        {'driver': 'SETP', 'value': 0, 'uom': 17, 'name': 'Start Temp'},
        {'driver': 'GV19', 'value': 0, 'uom': 44, 'name': 'Start Time'},
        {'driver': 'GV20', 'value': 0, 'uom': 25, 'name': 'Vehicle State'},
        {'driver': 'GV21', 'value': 0, 'uom': 38, 'name': 'Milage Meters'},
        {'driver': 'GV22', 'value': 0, 'uom': 25, 'name': 'Alarm Status'},
        {'driver': 'GV23', 'value': 0, 'uom': 25, 'name': 'Privacy Mode'},

    ]

    id = 'landnode'

    commands = {
        'DISCOVER': query,
        'DOORS': lckunlck,
        'ALARM': alrmreset,
        'BEEP': beep,
        'START': strt,
        'STOP': stp,
        'TEMP': dim,
        'PRIV': privacy,

    }
