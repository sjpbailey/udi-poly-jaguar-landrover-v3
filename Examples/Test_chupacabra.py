
import jlrpy
import json

# Authenticate using the username and password
c = jlrpy.Connection('sjpbailey@comcast.net', 'MyRover61!72')#'my@email.com', 'password'
v = c.vehicles[0]
got = v.get_attributes()
print(got['nickname'])
print(got['modelYear'])
print(got['vehicleBrand'])
print(got['vehicleType'])
#got = json.dumps(go)#, indent=4)
#print(got,'nickname')
#for i in got:

        #print(i)

# Get current active statuses
#v.lock(4442)
#c.get_user_info()
#p = c.get_user_info()
#go = v.get_status()
#go = json.dumps(go, indent=4)
#print(go)
#v.set_rcc_target_value(4442, 28)

#### "CLIMATE_STATUS_VENTING_TIME" "CLIMATE_STATUS_REMAINING_RUNTIME"
#go = v.get_status("THEFT_ALARM_STATUS")
##go = v.get_position()
#go = json.dumps(go, indent=4)
#print(go)  # dict

#for i in go['trips']["tripDetails"]:
#        print(i)


#v.get_status("TYRE_PRESSURE_REAR_RIGHT")
#for i in go["vehicleAlerts"]: #["vehicleStatus"]["coreStatus"]["vehicleAlerts"]:
#   print(i)
    # print()
    #print(i['key'])
#    print()
    #print(i['value'])
#    print()
    #print(i['value']['TU_STATUS_SERIAL_NUMBER'])
    # print(i['value'])"""
#v.get_status("TU_STATUS_PRIMARY_VOLT")

#for i in go["vehicleStatus"]["coreStatus"][29:30]:
#    print(i)
#    print(i['value'])    

# Ledgend of calls
# TU_STATUS_PRIMARY_VOLT = for i in go["vehicleStatus"]["coreStatus"][0:1]
# TU_STATUS_PRIMARY_CHARGE_PERCENT = [1:2]
# DOOR_IS_ALL_DOORS_LOCKED = [3:4] ############# DOORS
# U_STATUS_GSM_MODEM = [2:3]
# TU_STATUS_IMEI = [4:5]
# CLIMATE_STATUS_TIMER1_DAY = [5:6]
# BATTERY_STATUS = [6:7]
# WASHER_FLUID_WARN = [7:8]
# DOOR_FRONT_LEFT_POSITION = [8:9] ############# DOORS
# DOOR_REAR_RIGHT_POSITION = [9:10] ############# DOORS
# TU_STATUS_GNSS_ANTENNA = [10:11]
# TU_STATUS_SLEEP_CYCLES_START_TIME = [11:12]
# ENGINE_COOLANT_TEMP = [12:13]
# DISTANCE_TO_EMPTY_FUEL = [13:14]
# CLIMATE_STATUS_REMAINING_RUNTIME = [14:15]
# ODOMETER_MILES_RESOLUTION = [15:16]
# SERVICE_MODE_START = [16:17]
# TYRE_STATUS_REAR_LEFT = [17:18]
# ODOMETER_MILES = [18:19]
# TU_STATUS_SECONDARY_VOLT = [19:20]
# SRS_STATUS = [20:21]
        # DOOR_REAR_RIGHT_LOCK_STATUS = [21:22] ############# DOORS
# IS_PANIC_ALARM_TRIGGERED = [22:23]
# BATTERY_STATUS_12V_HEALTH = [23:24]
        # DOOR_FRONT_RIGHT_POSITION = [24:25] ############# DOORS
# BRAKE_FLUID_WARN = [25:26]
        # DOOR_REAR_LEFT_LOCK_STATUS = [26:27] ############# DOORS
# TU_STATUS_MOBILE_PHONE_CONNECTED = [27:28]
# BATTERY_STATUS_12V_ESTIMATE = [28:29]
# EXT_OIL_LEVEL_WARN = [29:30]        ############### OIL
# TU_STATUS_MIC = [30:31]
        # DOOR_ENGINE_HOOD_POSITION = [31:32] ############# DOORS
# TU_STATUS_POWER = [32:33]
# TRANSPORT_MODE_START = [33:34]
# EXT_BULB_STATUS_LEFT_TURN_ANY = [34:35]
# ENG_COOLANT_LEVEL_WARN = [35:36]
# WINDOW_FRONT_RIGHT_STATUS = [36:37] ############## Window
# WINDOW_REAR_RIGHT_STATUS = [37:38] ############## Window
# TU_STATUS_INT_RTC = [38:39]
# TYRE_STATUS_FRONT_LEFT = [39:40]
# THEFT_ALARM_STATUS = [40:41]
                                                    # IS_SUNROOF_OPEN = [41:42]
# ODOMETER" = [42:43]
# EXT_KILOMETERS_TO_SERVICE = [43:44]
# TU_STATUS_DAYS_SINCE_GNSS_FIX = [44:45]
# TU_STATUS_BUTTONS = [45:46]
# BATTERY_STATUS_12V_SOC = [46:47]
# VEHICLE_STATE_TYPE = [47:48]
# DOOR_ENGINE_HOOD_LOCK_STATUS =[48:49] ############# DOORS
# TYRE_STATUS_FRONT_RIGHT = [49:50]
# PRIVACY_SWITCH = [50:51]
# TU_STATUS_EXT_POWER = [51:52]
# CLIMATE_STATUS_TIMER1_MINUTE = [52:53]
# LATEST_COMPLETE_CONFIG_UPDATE = [53:54]
# TU_STATUS_HANDSET = [54:55]
# BRAZIL_EVENT_MODE = [55:56]
# IS_CRASH_SITUATION = [56:57]
        # DOOR_FRONT_RIGHT_LOCK_STATUS = [57:58] ############# DOORS
# TYRE_PRESSURE_REAR_RIGHT = [58:59]
# TU_STATUS_CONFIG_VERSION = [59:60]
# CLIMATE_STATUS_TIMER2_DAY = [60:61]
        # DOOR_FRONT_LEFT_LOCK_STATUS = [61:62] ############# DOORS
# WINDOW_REAR_LEFT_STATUS = [62:63] ############## Window
# TU_STATUS_EXT_HANDSFREE = [63:64]
# CLIMATE_STATUS_FFH_REMAINING_RUNTIME = [64:65]
                                        # CLIMATE_STATUS_VENTING_TIME = [65:66] ####Start vent time
# TYRE_PRESSURE_FRONT_RIGHT = [66:67]
# FUEL_LEVEL_PERC = [67:68]
# CLIMATE_STATUS_TIMER2_MONTH = [68:69]
# DOOR_IS_BOOT_LOCKED = [69:70] ############# DOORS
# DOOR_BOOT_POSITION = [70:71] ############# DOORS
# IS_HEAD_LIGHTS_ON = [71:72]
# TU_STATUS_CRASH_INPUT = [72:73]
# SERVICE_MODE_STOP = [73:74]
# TYRE_PRESSURE_FRONT_LEFT = [74:75]
# CLIMATE_STATUS_TIMER2_MINUTE = [75:76]
# IS_CAB_OPEN = [76:77]
# TU_STATUS_USES_EXTERNAL_GNSS = [77:78]
# ODOMETER_METER_RESOLUTION = [78:79]
# TU_STATUS_GSM_EXT_ANTENNA = [79:80]
# CLIMATE_STATUS_TIMER2_HOUR = [80:81]
# ODOMETER_METER = [81:82]
# BATTERY_VOLTAGE = for i in go["vehicleStatus"]["coreStatus"][82:83]
# TU_STATUS_SPEAKER = [83:84]
# TRANSPORT_MODE_STOP = [84:85]
# ENGINE_BLOCK = [85:86]
# TYRE_PRESSURE_REAR_LEFT = [86:87]
# CLIMATE_STATUS_TIMER_ACTIVATION_STATUS = [87:88]
# TU_STATUS_GNSS = [88:89]
# TU_STATUS_SW_VERSION_MAIN = [89:90]
# TU_STATUS_INT_POWER = [90:91]
# TU_STATUS_HW_VERSION = [91:92]
# WINDOW_FRONT_LEFT_STATUS = [92:93] ############## Window
# DOOR_REAR_LEFT_POSITION = [93:94] ############## DOORS
# CLIMATE_STATUS_OPERATING_STATUS = [94:95]
# CLIMATE_STATUS_TIMER1_HOUR = [95:96]
# CLIMATE_STATUS_TIMER1_MONTH = [96:97]
# TU_STATUS_SERIAL_NUMBER = [97:98]
# TYRE_STATUS_REAR_RIGHT = [98:99]
# TU_ACTIVATION_STATUS = [99:100]
# DOOR_BOOT_LOCK_STATUS = [100:101] ############# DOORS
# U_STATUS_CAN = [101:102]
#go = json.dumps(go, indent=4)
#print(go)
#trips = v.get_trips()
#print('\n')
#trips = json.dumps(trips, indent=4)
# Writing to sample.json
#with open("trips.json", "w") as outfile:
#    outfile.write(trips)
#print(trips)
#size = len(v.get_trips()["trips"])
#print(size) #### Total amount of trips
print('\n')
"""for i in v.get_trips()["trips"]:#[size-4:size-3]:
    #print(i)
    #print('/n')
    #print(i['id'])
    #print(i['routeDetails'])
    #print(i['tripDetails']['startPosition']['address'])
    #print(i['tripDetails']['endPosition']['address'])
    #print('\n')
    #print(int(i['tripDetails']['startOdometer']*0.00062137))
    #print(int(i['tripDetails']['endOdometer']*0.00062137))
    #print('\n')
    speed = int(i['tripDetails']['averageSpeed'])
    avgspd = speed
    print(avgspd)
    
    #print(int(i['tripDetails']['averageFuelConsumption']))
    #print(i['tripDetails']['startTime'])
    #print(i['tripDetails']['endTime'])"""




"""print(type(go)) #(str)
for i in go: #["coreStatus"]: #["vehicleStatus"]: #["coreStatus"]:
    print(i[0])
    #print()
    #print(i['key'])
    #print()
    #print(i['value'])
    #print()
    # print(i['value']['TU_STATUS_SERIAL_NUMBER'])
    #print(i['value'])"""


# print(go)
# locked = v.get_status("DOOR_BOOT_LOCK_STATUS")
# print(locked)
# Optionally, you can also specify a status value key
# battery = v.get_status("BATTERY_VOLTAGE")
# doors_locked= v.get_status("DOOR_IS_ALL_DOORS_LOCKED")
# odometer= v.get_status("ODOMETER_MILES")
# Get trip data (last 1000 trips).
# v.get_trips()
# battery = json.dumps(battery, indent=4)
# print(battery, doors_locked, odometer)
# doors_locked = json.dumps(doors_locked, indent=4)
# print(doors_locked)
# fuelLevel = json.dumps(fuelLevel, indent=4)
# print(fuelLevel)


"""import requests

url = "https://if9.prod-row.jlrmotor.com/if9/jlr/vehicles/{{SALEXEEU5P2223801}}/trips/export"

payload = json.dumps({"id": ["{{1691545310205}}"]})
headers = {
  'Content-Type': 'application/vnd.wirelesscar.ngtp.if9.TripIdList+json',
  'X-Device-Id': '{{e07652ed-b5f0-42f4-a715-4c68f6af7f0b}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)"""