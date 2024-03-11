import json
import Examples.jlrpy as jlrpy
import requests


# First Example

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YXM6YXNwYXNz',
    'X-Device-Id': '2c2a7d02-ebcc-41cf-a914-2e36307897f8',
    'Connection': 'close',
}

json_data = {
    'grant_type': 'password',
    'password': 'Password',
    'username': 'sjpbailey@comcast.net',
}

response = requests.post(
    'https://ifas.prod-row.jlrmotor.com/ifas/jlr/tokens', headers=headers, json=json_data)


print()
print(response)
print(response.text)
print()
response = json.dumps(response.json(), indent=4, sort_keys=True)
print(response)
# print(response.get())


c = jlrpy.Connection(email='sjpbailey@comcast.net',
                     refresh_token='48a83fd0-a125-4911-a341-745d0fb83ca9')
# c = jlrpy.Connection('sjpbailey@comcast.net', 'Password',
#                     '2c2a7d02-ebcc-41cf-a914-2e36307897f8')
# v = c.vehicles[0]
# print(v)


headers = {
    'X-Device-Id': '{{deviceId}}',
    'Content-Type': 'application/json',
    'Connection': 'close',
}

data = '{\n    "access_token": "{{access_token}}",\n    "authorization_token": "{{authorization_token}}",\n    "expires_in": "{{expires_in}}",\n    "deviceID":"{{deviceId}}"\n}+'

response = requests.post(
    'https://ifop.prod-row.jlrmotor.com/ifop/jlr/users/{{username}}/clients', headers=headers, data=data)


# Second
'''json_data = {
    'grant_type': 'refresh_token',
    'refresh_token': 'b973af3c-67f2-41c9-8498-f8b7a5883c16',
}

response = requests.post(
    'https://ifas.prod-row.jlrmotor.com/ifas/jlr/tokens', headers=headers, json=json_data)
print(response)

print(response.text)'''


'''headers = {
    'Accept': 'application/vnd.ngtp.org.if9.healthstatus-v2+json',
    'Content-Type': 'application/json',
    'X-Device-Id': '2c2a7d02-ebcc-41cf-a914-2e36307897f8',

}

response = requests.get(
    'https://if9.prod-row.jlrmotor.com/if9/jlr/vehicles/{{vin}}/attributes  ', headers=headers)

print(response)'''


'''headers = {
    'Accept': 'application/vnd.wirelesscar.ngtp.if9.User-v3+json',
    'Content-Type': 'application/json',
    'X-Device-Id': '2c2a7d02-ebcc-41cf-a914-2e36307897f8',
}

response = requests.get(
    'https://if9.prod-row.jlrmotor.com/if9/jlr/users?loginName=sjpbailey@comcast.net', headers=headers)'''


'''print("Tokens ")
print()
print("Access Token:  {}".format(data["access_token"]))
print()
print("Auth Token:  {}".format(data["authorization_token"]))
print()
print("Expires in:  {}".format(data["expires_in"]))
print()
print("Refresh Token:  {}".format(data["refresh_token"]))
print()
print("Token Type:  {}".format(data["token_type"]))
print()'''
# for i in response:
#    print(i)


'''json_data = {
    'grant_type': 'refresh_token',
    'refresh_token': '2c2a7d02-ebcc-41cf-a914-2e36307897f8',
}

response = requests.post(
    'https://ifas.prod-row.jlrmotor.com/ifas/jlr/tokens', headers=headers, json=json_data)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(response.text)
print(response)
print(response)'''


# vin = salexeeu5p2223801
# vin = SALEXEEU5P2223801
# refresh_token = '2c2a7d02-ebcc-41cf-a914-2e36307897f8'
# c = jlrpy.Connection('sjpbailey@comcast.net',
#                     '28d6c59f-8791-4e71-90f9-b3c2b8b92202',)

# c = jlrpy.Connection(email='sjpbailey@comcast.net',
#                     refresh_token='2c2a7d02-ebcc-41cf-a914-2e36307897f8')
#                     '2cbcac9a-c5fc-4743-ac10-a32bc155485e')
# c.get_user_info()
# print(c.text)

#
# refresh_token='66f41ec0-1897-4fe5-9d82-3f418914b474')
# v = c.vehicles[0]
# email = 'sjpbailey@comcast.net'
# refresh_token = '2cbcac9a-c5fc-4743-ac10-a32bc155485e'
# c = jlrpy.Connection(email, refresh_token)

"""status = {"vehicleStatus":
          {"coreStatus": [{"key": "TU_STATUS_PRIMARY_VOLT", "value": "4.1000000000000005"}, {"key": "TU_STATUS_PRIMARY_CHARGE_PERCENT", "value": "96"},
                          {"key": "DOOR_IS_ALL_DOORS_LOCKED", "value": "TRUE"}, {"key": "TU_STATUS_GSM_MODEM",
                                                                                 "value": "FUNCTIONING"}, {"key": "TU_STATUS_IMEI", "value": "357098161266799"},
                          {"key": "CLIMATE_STATUS_TIMER1_DAY", "value": "0"}, {"key": "BATTERY_STATUS",
                                                                               "value": "BATTERY_1_1"}, {"key": "WASHER_FLUID_WARN", "value": "NORMAL"},
                          {"key": "DOOR_FRONT_LEFT_POSITION", "value": "CLOSED"}, {"key": "DOOR_REAR_RIGHT_POSITION",
                                                                                   "value": "CLOSED"}, {"key": "TU_STATUS_GNSS_ANTENNA", "value": "UNCERTAIN"},
                          {"key": "TU_STATUS_SLEEP_CYCLES_START_TIME", "value": "0"}, {
              "key": "ENGINE_COOLANT_TEMP", "value": "93"}, {"key": "DISTANCE_TO_EMPTY_FUEL", "value": "479"},
              {"key": "CLIMATE_STATUS_REMAINING_RUNTIME", "value": "30"}, {"key": "ODOMETER_MILES_RESOLUTION",
                                                                           "value": "false"}, {"key": "SERVICE_MODE_START", "value": "1970-01-01T00:00:00+0000"},
              {"key": "TYRE_STATUS_REAR_LEFT", "value": "NORMAL"}, {"key": "ODOMETER_MILES", "value": "1724"}, {
                  "key": "TU_STATUS_SECONDARY_VOLT", "value": "0.0"}, {"key": "SRS_STATUS", "value": "SRS_NOT_DEPLOYED"},
              {"key": "DOOR_REAR_RIGHT_LOCK_STATUS", "value": "LOCKED"}, {"key": "IS_PANIC_ALARM_TRIGGERED", "value": "UNKNOWN"}, {
                  "key": "BATTERY_STATUS_12V_HEALTH", "value": "NONE"}, {"key": "DOOR_FRONT_RIGHT_POSITION", "value": "CLOSED"},
              {"key": "BRAKE_FLUID_WARN", "value": "NORMAL"}, {"key": "DOOR_REAR_LEFT_LOCK_STATUS", "value": "LOCKED"}, {
                  "key": "TU_STATUS_MOBILE_PHONE_CONNECTED", "value": "FALSE"}, {"key": "BATTERY_STATUS_12V_ESTIMATE", "value": "ACCURATE"},
              {"key": "EXT_OIL_LEVEL_WARN", "value": "NORMAL"}, {"key": "TU_STATUS_MIC", "value": "UNCERTAIN"}, {
                  "key": "DOOR_ENGINE_HOOD_POSITION", "value": "CLOSED"}, {"key": "TU_STATUS_POWER", "value": "MAIN_BATTERY"},
              {"key": "TRANSPORT_MODE_START", "value": "1970-01-01T00:00:00+0000"}, {"key": "EXT_BULB_STATUS_LEFT_TURN_ANY",
                                                                                     "value": "0"}, {"key": "ENG_COOLANT_LEVEL_WARN", "value": "NORMAL"},
              {"key": "WINDOW_FRONT_RIGHT_STATUS", "value": "CLOSED"}, {"key": "WINDOW_REAR_RIGHT_STATUS", "value": "CLOSED"}, {
                  "key": "TU_STATUS_INT_RTC", "value": "UNCERTAIN"}, {"key": "TYRE_STATUS_FRONT_LEFT", "value": "NORMAL"},
              {"key": "THEFT_ALARM_STATUS", "value": "ALARM_ARMED"}, {"key": "IS_SUNROOF_OPEN", "value": "FALSE"}, {
                  "key": "ODOMETER", "value": "2775000"}, {"key": "EXT_KILOMETERS_TO_SERVICE", "value": "31227"},
              {"key": "TU_STATUS_DAYS_SINCE_GNSS_FIX", "value": "0"}, {"key": "TU_STATUS_BUTTONS", "value": "UNCERTAIN"}, {
                  "key": "BATTERY_STATUS_12V_SOC", "value": "79"}, {"key": "VEHICLE_STATE_TYPE", "value": "KEY_REMOVED"},
              {"key": "DOOR_ENGINE_HOOD_LOCK_STATUS", "value": "LOCKED"}, {"key": "TYRE_STATUS_FRONT_RIGHT", "value": "NORMAL"}, {
                  "key": "PRIVACY_SWITCH", "value": "FALSE"}, {"key": "TU_STATUS_EXT_POWER", "value": "FUNCTIONING"},
              {"key": "CLIMATE_STATUS_TIMER1_MINUTE", "value": "0"}, {"key": "LATEST_COMPLETE_CONFIG_UPDATE", "value": "2023-08-05T14:12:39+0000"}, {
                  "key": "TU_STATUS_HANDSET", "value": "UNCERTAIN"}, {"key": "BRAZIL_EVENT_MODE", "value": "FALSE"},
              {"key": "IS_CRASH_SITUATION", "value": "FALSE"}, {"key": "DOOR_FRONT_RIGHT_LOCK_STATUS", "value": "LOCKED"}, {
                  "key": "TYRE_PRESSURE_REAR_RIGHT", "value": "3733"}, {"key": "TU_STATUS_CONFIG_VERSION", "value": "6"},
              {"key": "CLIMATE_STATUS_TIMER2_DAY", "value": "0"}, {"key": "DOOR_FRONT_LEFT_LOCK_STATUS", "value": "LOCKED"}, {
                  "key": "WINDOW_REAR_LEFT_STATUS", "value": "CLOSED"}, {"key": "TU_STATUS_EXT_HANDSFREE", "value": "UNCERTAIN"},
              {"key": "CLIMATE_STATUS_FFH_REMAINING_RUNTIME", "value": "0"}, {"key": "CLIMATE_STATUS_VENTING_TIME", "value": "30"}, {
                  "key": "TYRE_PRESSURE_FRONT_RIGHT", "value": "3376"}, {"key": "FUEL_LEVEL_PERC", "value": "90"},
              {"key": "CLIMATE_STATUS_TIMER2_MONTH", "value": "0"}, {"key": "DOOR_IS_BOOT_LOCKED", "value": "TRUE"}, {
                  "key": "DOOR_BOOT_POSITION", "value": "CLOSED"}, {"key": "IS_HEAD_LIGHTS_ON", "value": "UNKNOWN"},
              {"key": "TU_STATUS_CRASH_INPUT", "value": "UNCERTAIN"}, {"key": "SERVICE_MODE_STOP", "value": "1970-01-01T00:00:00+0000"}, {
                  "key": "TYRE_PRESSURE_FRONT_LEFT", "value": "3349"}, {"key": "CLIMATE_STATUS_TIMER2_MINUTE", "value": "0"},
              {"key": "IS_CAB_OPEN", "value": "FALSE"}, {"key": "TU_STATUS_USES_EXTERNAL_GNSS", "value": "FALSE"}, {
                  "key": "ODOMETER_METER_RESOLUTION", "value": "true"}, {"key": "TU_STATUS_GSM_EXT_ANTENNA", "value": "UNCERTAIN"},
              {"key": "CLIMATE_STATUS_TIMER2_HOUR", "value": "0"}, {"key": "ODOMETER_METER", "value": "2775000"}, {
                  "key": "BATTERY_VOLTAGE", "value": "12.6"}, {"key": "TU_STATUS_SPEAKER", "value": "UNCERTAIN"},
              {"key": "TRANSPORT_MODE_STOP", "value": "1970-01-01T00:00:00+0000"}, {"key": "ENGINE_BLOCK",
                                                                                    "value": "NORMAL_UNBLOCKED"}, {"key": "TYRE_PRESSURE_REAR_LEFT", "value": "3623"},
              {"key": "CLIMATE_STATUS_TIMER_ACTIVATION_STATUS", "value": "FALSE"}, {"key": "TU_STATUS_GNSS", "value": "FUNCTIONING"}, {
                  "key": "TU_STATUS_SW_VERSION_MAIN", "value": "L8B2-70712-AAA"}, {"key": "TU_STATUS_INT_POWER", "value": "UNCERTAIN"},
              {"key": "TU_STATUS_HW_VERSION", "value": "L8B2-70719-DB"}, {"key": "WINDOW_FRONT_LEFT_STATUS", "value": "CLOSED"}, {
                  "key": "DOOR_REAR_LEFT_POSITION", "value": "CLOSED"}, {"key": "CLIMATE_STATUS_OPERATING_STATUS", "value": "OFF"},
              {"key": "CLIMATE_STATUS_TIMER1_HOUR", "value": "0"}, {"key": "CLIMATE_STATUS_TIMER1_MONTH", "value": "0"}, {
                  "key": "TU_STATUS_SERIAL_NUMBER", "value": "302VIZCG09989"}, {"key": "TYRE_STATUS_REAR_RIGHT", "value": "NORMAL"},
              {"key": "TU_ACTIVATION_STATUS", "value": "PROVISIONED"}, {"key": "DOOR_BOOT_LOCK_STATUS", "value": "LOCKED"}, {"key": "TU_STATUS_CAN", "value": "UNCERTAIN"}], "evStatus": [{"key": "EV_IS_PLUGGED_IN", "value": "UNKNOWN"},
                                                                                                                                                                                          {"key": "EV_IS_CHARGING", "value": "UNKNOWN"}, {"key": "EV_IS_PRECONDITIONING", "value": "UNKNOWN"}, {"key": "EV_CHARGE_TYPE", "value": "UNKNOWN"}]}, "vehicleAlerts": [{"key": "ALARM_UNARMED", "value": "true", "active": False, "lastUpdatedTime": "2023-08-05T21:33:59+0000"},
                                                                                                                                                                                                                                                                                                                                                                  {"key": "TRANSPORT_MODE", "value": "true", "active": False, "lastUpdatedTime": "2023-07-05T22:46:21+0000"}, {
                                                                                                                                                                                              "key": "DOOR_OPEN", "value": "true", "active": False, "lastUpdatedTime": "2023-08-05T21:33:57+0000"},
              {"key": "ENGINE_ON", "value": "true", "active": True, "lastUpdatedTime": "2023-08-05T20:59:21+0000"}, {
                                                                                                                                                                                              "key": "WINDOW_OPEN", "value": "true", "active": False, "lastUpdatedTime": "2023-08-05T21:29:45+0000"},
              {"key": "FUEL_LEVEL_LTRS", "value": "5", "active": True, "lastUpdatedTime": "2023-06-29T20:45:14+0000"}, {"key": "VEHICLE_UNLOCKED", "value": "true", "active": False, "lastUpdatedTime": "2023-08-05T21:33:59+0000"}],
          "lastUpdatedTimeVehicleAlert": "2023-08-05T21:33:59+0000", "lastUpdatedTime": "2023-08-05T22:27:46+0000"}

"""
"""go = 70 #v.get_status("get_rcc_target_value")

#go = go*1.8+32 
go = (go - 32) * 5.0/9.0
print(go)  # dict
#v.lock(1234)
go = v.get_status()
for milage in go["vehicleStatus"]['coreStatus'][50:51]:
    print(milage)
    #print(milage['key'])
    #print(i[1])
    #print(milage['value'])
    #if milage['value'] == 'NORMAL':
    #    print('Normal')
    #else:
    #    print('Alarm')"""

"""for milage in v["vehicleStatus"]['coreStatus'][18:19]:
    print(milage['key'])
    #print(i[1])
    print(milage['value'])
    
for battery in status["vehicleStatus"]['coreStatus'][82:83]:
    print(battery['key'])
    print(battery['value'])
    
for oilflud in status["vehicleStatus"]['coreStatus'][29:30]:
    print(oilflud['key'])
    print(oilflud['value'])
    
for coolant in status["vehicleStatus"]['coreStatus'][12:13]:
    print(coolant['key'])
    print(coolant['value'])
    
for coolvl in status["vehicleStatus"]['coreStatus'][35:36]:
    print(coolvl['key'])
    print(coolvl['value'])
    
for brkflud in status["vehicleStatus"]['coreStatus'][25:26]:
    print(brkflud['key'])
    print(brkflud['value'])
    
for washflud in status["vehicleStatus"]['coreStatus'][7:8]:
    print(washflud['key'])
    print(washflud['value'])
    
# Doors
for doorlck in status["vehicleStatus"]['coreStatus'][2:3]:
    print(doorlck['key'])
    print(doorlck['value'])

for dorlckfl in status["vehicleStatus"]['coreStatus'][61:62]:
    print(dorlckfl['key'])
    print(dorlckfl['value'])
    
for dorlckfr in status["vehicleStatus"]['coreStatus'][57:58]:
    print(dorlckfr['key'])
    print(dorlckfr['value'])
    
for dorlckrl in status["vehicleStatus"]['coreStatus'][26:27]:
    print(dorlckrl['key'])
    print(dorlckrl['value'])
    
for dorlckrr in status["vehicleStatus"]['coreStatus'][21:22]:
    print(dorlckrr['key'])
    print(dorlckrr['value'])

for hoodlck in status["vehicleStatus"]['coreStatus'][48:49]:
    print(hoodlck['key'])
    print(hoodlck['value'])
    
for bootlck in status["vehicleStatus"]['coreStatus'][69:70]:
    print(bootlck['key'])
    print(bootlck['value'])"""

f"""or i in v.get_trips()["trips"]:#[size-4:size-3]:
    #print(i)
    #print('/n')
    #print(i['id'])
    print(i['routeDetails'])
    print(i['tripDetails']['startPosition']['address'])
    print(i['tripDetails']['endPosition']['address'])
    #print('\n')
    #print(int(i['tripDetails']['startOdometer']*0.00062137))
    #print(int(i['tripDetails']['endOdometer']*0.00062137))
    #print('\n')
    speed = int(i['tripDetails']['averageSpeed'])
    speed = speed
    print(speed)"""
# v.enable_privacy_mode(4442)
# v.get_trips()


'''data = {
    "access_token": "d32272de-65ff-4015-b95a-f39383cdaf45",
    "authorization_token": "RSACVP:XPZK7Jl1RM0TX+awfOauTnykiZGkmjKJsiWjFXzcGzK2zM2ybw/F3wXW3KpePMlzo5v0KGDYWxBoF636BnBTfxd9+ftH99LtztfGXBBzkCzLMW9TWeT33s+Us7OSFBg8ZHmdX7NQb/mv1waD7gTSb84dHCT0JN49UhYGdDgtfZ5MN4z28OnfJO68uBSbMYoh5qOr4JB7FlKAHRHFeeOXwtkoKNuY0FFIhc15TgAEUgcGKBxdYBMVL7+UvUB07VpHicNEyvo65cm2a4yHhgiQzKMOykuQmWHgW8PTOCA5YRhMgDxJwiiD6kRfSTDJPWMhTSk6OkvAWHJ2K3C6QFBzuQ==",
    "expires_in": "86400",
    "refresh_token": "f551879f-b979-40f3-a918-cba766ed37ed",
    "token_type": "bearer"
}


print()
print("Tokens ")
print()
print("Access Token:  {}".format(data["access_token"]))
print()
print("Auth Token:  {}".format(data["authorization_token"]))
print()
print("Expires in:  {}".format(data["expires_in"]))
print()
print("Refresh Token:  {}".format(data["refresh_token"]))
print()
print("Token Type:  {}".format(data["token_type"]))
print()'''

# for i in data:
#    print(i[0])
# print(i["access_token"])
# print(i["authorization_token"])
# print(i["expires_in"])
# print(i["refresh_token"])
# print(i["token_type"])
