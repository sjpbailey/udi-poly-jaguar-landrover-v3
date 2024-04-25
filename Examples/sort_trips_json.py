import json
from Examples import jlrpy
'''trips = {
    "trips": [
        {
            "id": 1691977113351,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 75,
                "boundingBox": {
                    "minLongitude": -121.47660305555556,
                    "minLatitude": 37.714510833333335,
                    "maxLongitude": -121.43644055555555,
                    "maxLatitude": 37.72879416666667
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 5954,
                "startOdometer": 4338000,
                "startTime": "2023-08-14T01:25:30+0000",
                "startPosition": {
                    "latitude": 37.72485888888889,
                    "longitude": -121.43726555555556,
                    "address": "W Schulte Rd 872, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4344000,
                "endTime": "2023-08-14T01:38:33+0000",
                "endPosition": {
                    "latitude": 37.718135833333335,
                    "longitude": -121.46991138888889,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 98.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 27.358848000000002,
                "averageFuelConsumption": 18.376139303498814,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691976220284,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 65,
                "boundingBox": {
                    "minLongitude": -121.47668333333333,
                    "minLatitude": 37.714445833333336,
                    "maxLongitude": -121.43726694444445,
                    "maxLatitude": 37.72865
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 6115,
                "startOdometer": 4332000,
                "startTime": "2023-08-14T01:13:56+0000",
                "startPosition": {
                    "latitude": 37.718004444444446,
                    "longitude": -121.46987583333333,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4338000,
                "endTime": "2023-08-14T01:23:39+0000",
                "endPosition": {
                    "latitude": 37.724854444444446,
                    "longitude": -121.43726694444445,
                    "address": "W Schulte Rd 872, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 38.624256,
                "averageFuelConsumption": 18.96891799070845,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691894429161,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 156,
                "boundingBox": {
                    "minLongitude": -121.47658527777777,
                    "minLatitude": 37.706632222222225,
                    "maxLongitude": -121.41635444444445,
                    "maxLatitude": 37.73860972222222
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 13518,
                "startOdometer": 4319000,
                "startTime": "2023-08-13T02:13:23+0000",
                "startPosition": {
                    "latitude": 37.70690361111111,
                    "longitude": -121.4216775,
                    "address": "La Monte Ln 285, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4332000,
                "endTime": "2023-08-13T02:40:28+0000",
                "endPosition": {
                    "latitude": 37.718112222222224,
                    "longitude": -121.46996527777777,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 30.577536000000002,
                "averageFuelConsumption": 18.817166646782784,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691882024785,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 110,
                "boundingBox": {
                    "minLongitude": -121.47666222222222,
                    "minLatitude": 37.70670222222222,
                    "maxLongitude": -121.42077111111111,
                    "maxLatitude": 37.72144361111111
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 7724,
                "startOdometer": 4311000,
                "startTime": "2023-08-12T22:53:09+0000",
                "startPosition": {
                    "latitude": 37.718158333333335,
                    "longitude": -121.46983083333333,
                    "address": "Perry Ln 2929, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4319000,
                "endTime": "2023-08-12T23:13:44+0000",
                "endPosition": {
                    "latitude": 37.706935,
                    "longitude": -121.4216825,
                    "address": "La Monte Ln 285, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 93.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.4,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 22.530816,
                "averageFuelConsumption": 21.190502980611246,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691865006682,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 63,
                "boundingBox": {
                    "minLongitude": -121.47684694444445,
                    "minLatitude": 37.718021666666665,
                    "maxLongitude": -121.42824888888889,
                    "maxLatitude": 37.739734722222224
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 6920,
                "startOdometer": 4304000,
                "startTime": "2023-08-12T18:19:35+0000",
                "startPosition": {
                    "latitude": 37.73880194444445,
                    "longitude": -121.42824888888889,
                    "address": "W 10th St 111, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4311000,
                "endTime": "2023-08-12T18:30:06+0000",
                "endPosition": {
                    "latitude": 37.71811888888889,
                    "longitude": -121.46995361111111,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 90.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 40.2336,
                "averageFuelConsumption": 14.519418708937335,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691861256564,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 89,
                "boundingBox": {
                    "minLongitude": -121.4766725,
                    "minLatitude": 37.71446972222222,
                    "maxLongitude": -121.42381611111111,
                    "maxLatitude": 37.73983166666667
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 8529,
                "startOdometer": 4295000,
                "startTime": "2023-08-12T17:14:32+0000",
                "startPosition": {
                    "latitude": 37.71823638888889,
                    "longitude": -121.46995861111111,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4303000,
                "endTime": "2023-08-12T17:27:36+0000",
                "endPosition": {
                    "latitude": 37.73983166666667,
                    "longitude": -121.42451222222222,
                    "address": "E 11th St 61, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 86.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.4,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 38.624256,
                "averageFuelConsumption": 18.520833313762584,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691807680373,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 58,
                "boundingBox": {
                    "minLongitude": -121.47681722222222,
                    "minLatitude": 37.71803055555556,
                    "maxLongitude": -121.44086666666666,
                    "maxLatitude": 37.742063888888886
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 5954,
                "startOdometer": 4289000,
                "startTime": "2023-08-12T02:24:42+0000",
                "startPosition": {
                    "latitude": 37.74129777777778,
                    "longitude": -121.44086666666666,
                    "address": "Audrey Dr 1235, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4295000,
                "endTime": "2023-08-12T02:34:40+0000",
                "endPosition": {
                    "latitude": 37.718115833333336,
                    "longitude": -121.46996472222222,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 86.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 37.014912,
                "averageFuelConsumption": 17.553327095879464,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691806964855,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 470,
                "boundingBox": {
                    "minLongitude": -121.44086944444444,
                    "minLatitude": 36.253545,
                    "maxLongitude": -120.24219916666667,
                    "maxLatitude": 37.7412825
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 196661,
                "startOdometer": 4092000,
                "startTime": "2023-08-12T00:31:49+0000",
                "startPosition": {
                    "latitude": 36.25379777777778,
                    "longitude": -120.24951277777778,
                    "address": "W Dorris Ave 25145, 93210 Coalinga, United States",
                    "postalCode": "93210",
                    "city": "Coalinga",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4289000,
                "endTime": "2023-08-12T02:22:44+0000",
                "endPosition": {
                    "latitude": 37.741278333333334,
                    "longitude": -121.44086472222222,
                    "address": "Audrey Dr 1235, 95376 Tracy, United States",
                    "postalCode": "95376",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 45.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 2.1,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 3.6,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 107.82604800000001,
                "averageFuelConsumption": 14.000868040761,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691798608861,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 451,
                "boundingBox": {
                    "minLongitude": -120.25033583333334,
                    "minLatitude": 34.793596111111114,
                    "maxLongitude": -118.85213888888889,
                    "maxLatitude": 36.254442222222224
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 204869,
                "startOdometer": 3887000,
                "startTime": "2023-08-11T22:14:59+0000",
                "startPosition": {
                    "latitude": 34.79421277777778,
                    "longitude": -118.85264027777778,
                    "address": "Gorman School Rd 49726, 93243 Lebec, United States",
                    "postalCode": "93243",
                    "city": "Lebec",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 4092000,
                "endTime": "2023-08-12T00:03:28+0000",
                "endPosition": {
                    "latitude": 36.253725,
                    "longitude": -120.25033583333334,
                    "address": "W Dorris Ave 25203, 93210 Coalinga, United States",
                    "postalCode": "93210",
                    "city": "Coalinga",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 42.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 2.0,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 3.0,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 114.26342400000001,
                "averageFuelConsumption": 12.187284097657242,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691791797858,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 403,
                "boundingBox": {
                    "minLongitude": -118.85265111111111,
                    "minLatitude": 34.2368125,
                    "maxLongitude": -118.46745638888889,
                    "maxLatitude": 34.7955725
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 108952,
                "startOdometer": 3778000,
                "startTime": "2023-08-11T20:40:37+0000",
                "startPosition": {
                    "latitude": 34.2368125,
                    "longitude": -118.80065194444444,
                    "address": "Dusty Rose Ct 135, 93065 Simi Valley, United States",
                    "postalCode": "93065",
                    "city": "Simi Valley",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3887000,
                "endTime": "2023-08-11T22:09:57+0000",
                "endPosition": {
                    "latitude": 34.794225,
                    "longitude": -118.85265111111111,
                    "address": "Gorman School Rd 49726, 93243 Lebec, United States",
                    "postalCode": "93243",
                    "city": "Lebec",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 60.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 2.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.0,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 74.029824,
                "averageFuelConsumption": 14.084705573939212,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691783968635,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 159,
                "boundingBox": {
                    "minLongitude": -118.87787527777778,
                    "minLatitude": 34.13599694444444,
                    "maxLongitude": -118.80047916666666,
                    "maxLatitude": 34.254124166666664
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 23979,
                "startOdometer": 3754000,
                "startTime": "2023-08-11T19:33:56+0000",
                "startPosition": {
                    "latitude": 34.13682083333333,
                    "longitude": -118.86961916666667,
                    "address": "Lower Lake Rd 361, 91361 Westlake Village, United States",
                    "postalCode": "91361",
                    "city": "Westlake Village",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3778000,
                "endTime": "2023-08-11T19:59:28+0000",
                "endPosition": {
                    "latitude": 34.236802777777775,
                    "longitude": -118.80066055555555,
                    "address": "Dusty Rose Ct 134, 93065 Simi Valley, United States",
                    "postalCode": "93065",
                    "city": "Simi Valley",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 68.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 3.3,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 56.327040000000004,
                "averageFuelConsumption": 13.518079487631313,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691780412197,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 420,
                "boundingBox": {
                    "minLongitude": -118.87808444444444,
                    "minLatitude": 33.694922222222225,
                    "maxLongitude": -117.95332694444444,
                    "maxLatitude": 34.173720277777775
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 119574,
                "startOdometer": 3634000,
                "startTime": "2023-08-11T17:26:03+0000",
                "startPosition": {
                    "latitude": 33.694922222222225,
                    "longitude": -117.95451138888889,
                    "address": "Brookhurst St 18471, 92708 Fountain Valley, United States",
                    "postalCode": "92708",
                    "city": "Fountain Valley",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3754000,
                "endTime": "2023-08-11T19:00:11+0000",
                "endPosition": {
                    "latitude": 34.13683805555556,
                    "longitude": -118.86962416666667,
                    "address": "Lower Lake Rd 363, 91361 Westlake Village, United States",
                    "postalCode": "91361",
                    "city": "Westlake Village",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 77.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 3.8,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 77.248512,
                "averageFuelConsumption": 12.445216036232,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691772699371,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 187,
                "boundingBox": {
                    "minLongitude": -117.96385222222223,
                    "minLatitude": 33.53749055555556,
                    "maxLongitude": -117.77964638888889,
                    "maxLatitude": 33.69513361111111
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 27519,
                "startOdometer": 3607000,
                "startTime": "2023-08-11T16:09:56+0000",
                "startPosition": {
                    "latitude": 33.53869944444445,
                    "longitude": -117.78085027777777,
                    "address": "Sleepy Hollow Ln 620, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3634000,
                "endTime": "2023-08-11T16:51:39+0000",
                "endPosition": {
                    "latitude": 33.69491194444444,
                    "longitude": -117.95451111111112,
                    "address": "Brookhurst St 18471, 92708 Fountain Valley, United States",
                    "postalCode": "92708",
                    "city": "Fountain Valley",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 85.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.2,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 40.2336,
                "averageFuelConsumption": 13.067476838043602,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691725305600,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 141,
                "boundingBox": {
                    "minLongitude": -117.78528805555555,
                    "minLatitude": 33.53853194444444,
                    "maxLongitude": -117.69799805555556,
                    "maxLatitude": 33.620491111111114
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 13840,
                "startOdometer": 3593000,
                "startTime": "2023-08-11T03:15:34+0000",
                "startPosition": {
                    "latitude": 33.61775361111111,
                    "longitude": -117.69908777777778,
                    "address": "Landisview Ave 23801, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3607000,
                "endTime": "2023-08-11T03:41:45+0000",
                "endPosition": {
                    "latitude": 33.53853194444444,
                    "longitude": -117.78077277777778,
                    "address": "Sleepy Hollow Ln 636, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 87.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.4,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 32.18688,
                "averageFuelConsumption": 14.70091144279905,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691720974421,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 41,
                "boundingBox": {
                    "minLongitude": -117.70459472222223,
                    "minLatitude": 33.617735277777776,
                    "maxLongitude": -117.69749277777778,
                    "maxLatitude": 33.628009444444444
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 1770,
                "startOdometer": 3591000,
                "startTime": "2023-08-11T02:24:12+0000",
                "startPosition": {
                    "latitude": 33.62778888888889,
                    "longitude": -117.70399,
                    "address": "Muirlands Blvd 24406, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3593000,
                "endTime": "2023-08-11T02:29:34+0000",
                "endPosition": {
                    "latitude": 33.617735277777776,
                    "longitude": -117.69907638888888,
                    "address": "Landisview Ave 23801, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 94.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 19.312128,
                "averageFuelConsumption": 24.001488069876,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691716368042,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 34,
                "boundingBox": {
                    "minLongitude": -117.70400555555555,
                    "minLatitude": 33.6177625,
                    "maxLongitude": -117.69733138888888,
                    "maxLatitude": 33.62803916666667
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 1609,
                "startOdometer": 3589000,
                "startTime": "2023-08-11T01:07:09+0000",
                "startPosition": {
                    "latitude": 33.61778388888889,
                    "longitude": -117.69900805555555,
                    "address": "Landisview Ave 23791, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3591000,
                "endTime": "2023-08-11T01:12:47+0000",
                "endPosition": {
                    "latitude": 33.62779666666667,
                    "longitude": -117.70400083333334,
                    "address": "Muirlands Blvd 24406, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 17.702784,
                "averageFuelConsumption": 27.036158975262627,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691712226501,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 42,
                "boundingBox": {
                    "minLongitude": -117.72463861111112,
                    "minLatitude": 33.610236666666665,
                    "maxLongitude": -117.69903444444445,
                    "maxLatitude": 33.620309722222224
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 2896,
                "startOdometer": 3586000,
                "startTime": "2023-08-10T23:55:51+0000",
                "startPosition": {
                    "latitude": 33.610236666666665,
                    "longitude": -117.72463861111112,
                    "address": "El Toro Rd 24362, 92637 Laguna Woods, United States",
                    "postalCode": "92637",
                    "city": "Laguna Woods",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3589000,
                "endTime": "2023-08-11T00:03:46+0000",
                "endPosition": {
                    "latitude": 33.61775277777778,
                    "longitude": -117.69906166666667,
                    "address": "Landisview Ave 23791, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 90.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 22.530816,
                "averageFuelConsumption": 22.616786835075462,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691711476724,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 139,
                "boundingBox": {
                    "minLongitude": -117.7825613888889,
                    "minLatitude": 33.537709444444445,
                    "maxLongitude": -117.72464138888888,
                    "maxLatitude": 33.61024027777778
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 10943,
                "startOdometer": 3575000,
                "startTime": "2023-08-10T23:21:28+0000",
                "startPosition": {
                    "latitude": 33.53805583333333,
                    "longitude": -117.78068888888889,
                    "address": "Sleepy Hollow Ln 653, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3586000,
                "endTime": "2023-08-10T23:51:16+0000",
                "endPosition": {
                    "latitude": 33.61024027777778,
                    "longitude": -117.72464138888888,
                    "address": "El Toro Rd 24362, 92637 Laguna Woods, United States",
                    "postalCode": "92637",
                    "city": "Laguna Woods",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 22.530816,
                "averageFuelConsumption": 22.83636728978493,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691614999913,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 102,
                "boundingBox": {
                    "minLongitude": -117.82587166666667,
                    "minLatitude": 33.53749,
                    "maxLongitude": -117.7797075,
                    "maxLatitude": 33.56580972222222
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 6276,
                "startOdometer": 3569000,
                "startTime": "2023-08-09T20:43:43+0000",
                "startPosition": {
                    "latitude": 33.561503333333334,
                    "longitude": -117.82127777777778,
                    "address": "N Coast Hwy 8809, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3575000,
                "endTime": "2023-08-09T21:03:19+0000",
                "endPosition": {
                    "latitude": 33.53843972222222,
                    "longitude": -117.78076472222222,
                    "address": "Sleepy Hollow Ln 633, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 90.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 19.312128,
                "averageFuelConsumption": 21.190502980611246,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691609463022,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 56,
                "boundingBox": {
                    "minLongitude": -117.85997083333334,
                    "minLatitude": 33.56132777777778,
                    "maxLongitude": -117.82053027777778,
                    "maxLatitude": 33.58936805555555
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 5149,
                "startOdometer": 3564000,
                "startTime": "2023-08-09T19:21:00+0000",
                "startPosition": {
                    "latitude": 33.58822888888889,
                    "longitude": -117.85993944444445,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3569000,
                "endTime": "2023-08-09T19:31:02+0000",
                "endPosition": {
                    "latitude": 33.561524444444444,
                    "longitude": -117.82127638888889,
                    "address": "N Coast Hwy 8809, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 94.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 25.749504,
                "averageFuelConsumption": 18.520833313762584,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691603618628,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 85,
                "boundingBox": {
                    "minLongitude": -117.85995055555556,
                    "minLatitude": 33.537482777777775,
                    "maxLongitude": -117.77964416666667,
                    "maxLatitude": 33.58945388888889
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 9656,
                "startOdometer": 3554000,
                "startTime": "2023-08-09T17:36:21+0000",
                "startPosition": {
                    "latitude": 33.53808166666666,
                    "longitude": -117.7807713888889,
                    "address": "Sleepy Hollow Ln 653, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3564000,
                "endTime": "2023-08-09T17:53:38+0000",
                "endPosition": {
                    "latitude": 33.58817638888889,
                    "longitude": -117.85995027777778,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 94.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 33.796224,
                "averageFuelConsumption": 14.342352627121027,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691598730163,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 63,
                "boundingBox": {
                    "minLongitude": -117.85996472222222,
                    "minLatitude": 33.538441666666664,
                    "maxLongitude": -117.7807763888889,
                    "maxLatitude": 33.58934305555555
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 9334,
                "startOdometer": 3544000,
                "startTime": "2023-08-09T16:19:37+0000",
                "startPosition": {
                    "latitude": 33.588188611111114,
                    "longitude": -117.85996472222222,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3554000,
                "endTime": "2023-08-09T16:32:09+0000",
                "endPosition": {
                    "latitude": 33.538441666666664,
                    "longitude": -117.78081972222222,
                    "address": "Sleepy Hollow Ln 633, 92651 Laguna Beach, United States",
                    "postalCode": "92651",
                    "city": "Laguna Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 96.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 43.452288,
                "averageFuelConsumption": 12.578319951058013,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691549827273,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 40,
                "boundingBox": {
                    "minLongitude": -117.85996972222222,
                    "minLatitude": 33.56832277777778,
                    "maxLongitude": -117.83134638888889,
                    "maxLatitude": 33.589462222222224
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 3540,
                "startOdometer": 3541000,
                "startTime": "2023-08-09T02:50:43+0000",
                "startPosition": {
                    "latitude": 33.568662777777774,
                    "longitude": -117.83135638888889,
                    "address": "E Coast Hwy 8032, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3544000,
                "endTime": "2023-08-09T02:57:06+0000",
                "endPosition": {
                    "latitude": 33.588182777777774,
                    "longitude": -117.85996972222222,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 91.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 33.796224,
                "averageFuelConsumption": 17.16894767042225,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691549233532,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 149,
                "boundingBox": {
                    "minLongitude": -117.83136361111112,
                    "minLatitude": 33.542880833333335,
                    "maxLongitude": -117.69800805555556,
                    "maxLatitude": 33.620495
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 18346,
                "startOdometer": 3522000,
                "startTime": "2023-08-09T02:18:53+0000",
                "startPosition": {
                    "latitude": 33.617804166666666,
                    "longitude": -117.69907083333334,
                    "address": "Landisview Ave 23791, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3541000,
                "endTime": "2023-08-09T02:47:13+0000",
                "endPosition": {
                    "latitude": 33.568666666666665,
                    "longitude": -117.83136361111112,
                    "address": "E Coast Hwy 8032, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 79.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 3.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 38.624256,
                "averageFuelConsumption": 13.21430242049353,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691545310205,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 274,
                "boundingBox": {
                    "minLongitude": -118.11226333333333,
                    "minLatitude": 33.61398555555556,
                    "maxLongitude": -117.69903194444444,
                    "maxLatitude": 33.77880138888889
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 48280,
                "startOdometer": 3474000,
                "startTime": "2023-08-09T00:39:38+0000",
                "startPosition": {
                    "latitude": 33.75870527777778,
                    "longitude": -118.11226333333333,
                    "address": "E Pacific Coast Hwy 6376, 90803 Long Beach, United States",
                    "postalCode": "90803",
                    "city": "Long Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3522000,
                "endTime": "2023-08-09T01:41:50+0000",
                "endPosition": {
                    "latitude": 33.61774805555556,
                    "longitude": -117.69908555555556,
                    "address": "Landisview Ave 23801, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 83.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.1,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 46.670976,
                "averageFuelConsumption": 13.755238776888,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691534984301,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 287,
                "boundingBox": {
                    "minLongitude": -118.11279944444445,
                    "minLatitude": 33.615316388888886,
                    "maxLongitude": -117.69826611111111,
                    "maxLatitude": 33.760040277777776
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 43452,
                "startOdometer": 3431000,
                "startTime": "2023-08-08T21:45:13+0000",
                "startPosition": {
                    "latitude": 33.617775,
                    "longitude": -117.69904527777778,
                    "address": "Landisview Ave 23791, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3474000,
                "endTime": "2023-08-08T22:49:43+0000",
                "endPosition": {
                    "latitude": 33.75871222222222,
                    "longitude": -118.11225694444444,
                    "address": "E Pacific Coast Hwy 6376, 90803 Long Beach, United States",
                    "postalCode": "90803",
                    "city": "Long Beach",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 92.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 38.624256,
                "averageFuelConsumption": 14.342352627121027,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691525918728,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 140,
                "boundingBox": {
                    "minLongitude": -117.859895,
                    "minLatitude": 33.54281972222222,
                    "maxLongitude": -117.69903194444444,
                    "maxLatitude": 33.62031916666667
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 21565,
                "startOdometer": 3409000,
                "startTime": "2023-08-08T19:49:23+0000",
                "startPosition": {
                    "latitude": 33.58819861111111,
                    "longitude": -117.85989277777777,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3431000,
                "endTime": "2023-08-08T20:18:38+0000",
                "endPosition": {
                    "latitude": 33.61776138888889,
                    "longitude": -117.69905972222222,
                    "address": "Landisview Ave 23791, 92630 Lake Forest, United States",
                    "postalCode": "92630",
                    "city": "Lake Forest",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 94.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 45.061632,
                "averageFuelConsumption": 14.084705573939212,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691519549462,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 88,
                "boundingBox": {
                    "minLongitude": -117.91942666666667,
                    "minLatitude": 33.58819361111111,
                    "maxLongitude": -117.85882333333333,
                    "maxLatitude": 33.63612805555555
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 8690,
                "startOdometer": 3400000,
                "startTime": "2023-08-08T18:15:00+0000",
                "startPosition": {
                    "latitude": 33.63597277777778,
                    "longitude": -117.91903166666667,
                    "address": "E 17th St 176, 92627 Costa Mesa, United States",
                    "postalCode": "92627",
                    "city": "Costa Mesa",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3409000,
                "endTime": "2023-08-08T18:32:29+0000",
                "endPosition": {
                    "latitude": 33.58819527777778,
                    "longitude": -117.85994416666666,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 30.577536000000002,
                "averageFuelConsumption": 17.295189932704766,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691512992316,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 87,
                "boundingBox": {
                    "minLongitude": -117.91568694444445,
                    "minLatitude": 33.588146944444446,
                    "maxLongitude": -117.85870777777778,
                    "maxLatitude": 33.63380194444444
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 8207,
                "startOdometer": 3391000,
                "startTime": "2023-08-08T16:25:30+0000",
                "startPosition": {
                    "latitude": 33.588188333333335,
                    "longitude": -117.85995555555556,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3400000,
                "endTime": "2023-08-08T16:43:12+0000",
                "endPosition": {
                    "latitude": 33.63380194444444,
                    "longitude": -117.91529944444444,
                    "address": "E 17th Pl 296, 92627 Costa Mesa, United States",
                    "postalCode": "92627",
                    "city": "Costa Mesa",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 27.358848000000002,
                "averageFuelConsumption": 17.295189932704766,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691458872814,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 36,
                "boundingBox": {
                    "minLongitude": -117.85995972222223,
                    "minLatitude": 33.57122,
                    "maxLongitude": -117.8360025,
                    "maxLatitude": 33.58947333333333
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 3540,
                "startOdometer": 3388000,
                "startTime": "2023-08-08T01:35:30+0000",
                "startPosition": {
                    "latitude": 33.57410138888889,
                    "longitude": -117.83943805555556,
                    "address": "E Coast Hwy 7701, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3391000,
                "endTime": "2023-08-08T01:41:12+0000",
                "endPosition": {
                    "latitude": 33.5881925,
                    "longitude": -117.85995972222223,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 91.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 35.405568,
                "averageFuelConsumption": 18.233688611223627,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691456514831,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 29,
                "boundingBox": {
                    "minLongitude": -117.85997611111111,
                    "minLatitude": 33.57409888888889,
                    "maxLongitude": -117.83943027777778,
                    "maxLatitude": 33.58937777777778
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 2574,
                "startOdometer": 3385000,
                "startTime": "2023-08-08T00:56:22+0000",
                "startPosition": {
                    "latitude": 33.58821277777778,
                    "longitude": -117.85997611111111,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3388000,
                "endTime": "2023-08-08T01:01:54+0000",
                "endPosition": {
                    "latitude": 33.57409888888889,
                    "longitude": -117.83944833333334,
                    "address": "E Coast Hwy 7701, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 25.749504,
                "averageFuelConsumption": 19.76593135166259,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691439533540,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 92,
                "boundingBox": {
                    "minLongitude": -117.85997944444445,
                    "minLatitude": 33.56702388888889,
                    "maxLongitude": -117.82954916666667,
                    "maxLatitude": 33.589468333333336
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 4345,
                "startOdometer": 3381000,
                "startTime": "2023-08-07T20:00:47+0000",
                "startPosition": {
                    "latitude": 33.57006944444444,
                    "longitude": -117.83294694444444,
                    "address": "E Coast Hwy 7942, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3385000,
                "endTime": "2023-08-07T20:18:53+0000",
                "endPosition": {
                    "latitude": 33.5881975,
                    "longitude": -117.85997916666666,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.7,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 14.484096000000001,
                "averageFuelConsumption": 25.847756382943388,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691436816138,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 43,
                "boundingBox": {
                    "minLongitude": -117.85995916666667,
                    "minLatitude": 33.56974527777778,
                    "maxLongitude": -117.83296388888888,
                    "maxLatitude": 33.58936083333333
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 3540,
                "startOdometer": 3377000,
                "startTime": "2023-08-07T19:26:03+0000",
                "startPosition": {
                    "latitude": 33.58823,
                    "longitude": -117.85995916666667,
                    "address": "Roxbury Rd 4627, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3381000,
                "endTime": "2023-08-07T19:33:35+0000",
                "endPosition": {
                    "latitude": 33.57006527777778,
                    "longitude": -117.83296388888888,
                    "address": "E Coast Hwy 7942, 92657 Newport Coast, United States",
                    "postalCode": "92657",
                    "city": "Newport Coast",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 95.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 27.358848000000002,
                "averageFuelConsumption": 20.632858165332003,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691431435723,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 710,
                "boundingBox": {
                    "minLongitude": -119.65945777777777,
                    "minLatitude": 33.58815527777778,
                    "maxLongitude": -117.85883833333334,
                    "maxLatitude": 35.61692194444444
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 296763,
                "startOdometer": 3081000,
                "startTime": "2023-08-07T15:14:21+0000",
                "startPosition": {
                    "latitude": 35.61692194444444,
                    "longitude": -119.65855055555555,
                    "address": "CA-46 21948, 93249 Lost Hills, United States",
                    "postalCode": "93249",
                    "city": "Lost Hills",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3377000,
                "endTime": "2023-08-07T18:03:55+0000",
                "endPosition": {
                    "latitude": 33.588258333333336,
                    "longitude": -117.8599886111111,
                    "address": "Roxbury Rd 4626, 92625 Corona del Mar, United States",
                    "postalCode": "92625",
                    "city": "Corona del Mar",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 70.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 3.4,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 106.21670400000001,
                "averageFuelConsumption": 12.645945327138966,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691420016006,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 388,
                "boundingBox": {
                    "minLongitude": -121.01686916666667,
                    "minLatitude": 35.61629333333333,
                    "maxLongitude": -119.65535472222223,
                    "maxLatitude": 37.10591361111111
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 200846,
                "startOdometer": 2880000,
                "startTime": "2023-08-07T13:20:25+0000",
                "startPosition": {
                    "latitude": 37.10024333333333,
                    "longitude": -121.01511638888888,
                    "address": "Santa Nella Rd 13032, 95322 Gustine, United States",
                    "postalCode": "95322",
                    "city": "Gustine",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 3081000,
                "endTime": "2023-08-07T14:53:35+0000",
                "endPosition": {
                    "latitude": 35.616732222222225,
                    "longitude": -119.65878444444445,
                    "address": "CA-46 21948, 93249 Lost Hills, United States",
                    "postalCode": "93249",
                    "city": "Lost Hills",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 40.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 1.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 2.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 130.356864,
                "averageFuelConsumption": 14.430342520538945,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691412818998,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 263,
                "boundingBox": {
                    "minLongitude": -121.53578055555556,
                    "minLatitude": 37.10004166666667,
                    "maxLongitude": -121.01503444444444,
                    "maxLatitude": 37.722165
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 89157,
                "startOdometer": 2791000,
                "startTime": "2023-08-07T11:53:46+0000",
                "startPosition": {
                    "latitude": 37.71813,
                    "longitude": -121.46998833333333,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2880000,
                "endTime": "2023-08-07T12:53:38+0000",
                "endPosition": {
                    "latitude": 37.100254722222225,
                    "longitude": -121.01511027777778,
                    "address": "Santa Nella Rd 13032, 95322 Gustine, United States",
                    "postalCode": "95322",
                    "city": "Gustine",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 74.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 3.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.1,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 88.51392000000001,
                "averageFuelConsumption": 12.511413993871532,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691284663610,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 75,
                "boundingBox": {
                    "minLongitude": -121.534505,
                    "minLatitude": 37.71803444444444,
                    "maxLongitude": -121.46900805555556,
                    "maxLatitude": 37.738996388888886
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 8046,
                "startOdometer": 2783000,
                "startTime": "2023-08-06T01:05:30+0000",
                "startPosition": {
                    "latitude": 37.738662222222224,
                    "longitude": -121.534505,
                    "address": "Promontory Pkwy 501, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2791000,
                "endTime": "2023-08-06T01:17:43+0000",
                "endPosition": {
                    "latitude": 37.71811666666667,
                    "longitude": -121.46997972222222,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 38.624256,
                "averageFuelConsumption": 15.577124707601644,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691283067904,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 59,
                "boundingBox": {
                    "minLongitude": -121.53452416666667,
                    "minLatitude": 37.71802805555556,
                    "maxLongitude": -121.469955,
                    "maxLatitude": 37.738643055555556
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 7724,
                "startOdometer": 2775000,
                "startTime": "2023-08-06T00:42:16+0000",
                "startPosition": {
                    "latitude": 37.7180975,
                    "longitude": -121.469955,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2783000,
                "endTime": "2023-08-06T00:51:07+0000",
                "endPosition": {
                    "latitude": 37.738643055555556,
                    "longitude": -121.53452055555556,
                    "address": "Promontory Pkwy 501, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 97.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 43.452288,
                "averageFuelConsumption": 18.520833313762584,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691271094806,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 142,
                "boundingBox": {
                    "minLongitude": -121.7586225,
                    "minLatitude": 37.69839861111111,
                    "maxLongitude": -121.46997666666667,
                    "maxLatitude": 37.741797777777776
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 27680,
                "startOdometer": 2747000,
                "startTime": "2023-08-05T21:02:57+0000",
                "startPosition": {
                    "latitude": 37.70146638888889,
                    "longitude": -121.758605,
                    "address": "Las Positas Rd 3538, 94551 Livermore, United States",
                    "postalCode": "94551",
                    "city": "Livermore",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2775000,
                "endTime": "2023-08-05T21:31:34+0000",
                "endPosition": {
                    "latitude": 37.71811527777778,
                    "longitude": -121.46997666666667,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 56.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 2.7,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 3.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 53.108352000000004,
                "averageFuelConsumption": 14.084705573939212,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691268849150,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 85,
                "boundingBox": {
                    "minLongitude": -121.90374527777777,
                    "minLatitude": 37.67682388888889,
                    "maxLongitude": -121.75858277777778,
                    "maxLatitude": 37.701458055555555
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 14323,
                "startOdometer": 2733000,
                "startTime": "2023-08-05T20:38:01+0000",
                "startPosition": {
                    "latitude": 37.67707027777778,
                    "longitude": -121.89821638888888,
                    "address": "Hopyard Rd 3127, 94588 Pleasanton, United States",
                    "postalCode": "94588",
                    "city": "Pleasanton",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2747000,
                "endTime": "2023-08-05T20:54:08+0000",
                "endPosition": {
                    "latitude": 37.701458055555555,
                    "longitude": -121.75860833333333,
                    "address": "Las Positas Rd 3538, 94551 Livermore, United States",
                    "postalCode": "94551",
                    "city": "Livermore",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 92.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.8,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 5.0,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 53.108352000000004,
                "averageFuelConsumption": 13.836151946163813,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691265351476,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 231,
                "boundingBox": {
                    "minLongitude": -121.89820666666667,
                    "minLatitude": 37.66083388888889,
                    "maxLongitude": -121.5319975,
                    "maxLatitude": 37.7228275
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 40555,
                "startOdometer": 2692000,
                "startTime": "2023-08-05T19:15:15+0000",
                "startPosition": {
                    "latitude": 37.722767222222224,
                    "longitude": -121.5319975,
                    "address": "International Pkwy 25441, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2733000,
                "endTime": "2023-08-05T19:55:51+0000",
                "endPosition": {
                    "latitude": 37.67708833333333,
                    "longitude": -121.89820666666667,
                    "address": "Hopyard Rd 3127, 94588 Pleasanton, United States",
                    "postalCode": "94588",
                    "city": "Pleasanton",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 86.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.3,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.5,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.6,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 61.155072000000004,
                "averageFuelConsumption": 13.518079487631313,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        },
        {
            "id": 1691262669051,
            "name": True,
            "category": True,
            "routeDetails": {
                "route": True,
                "totalWaypoints": 59,
                "boundingBox": {
                    "minLongitude": -121.53268888888888,
                    "minLatitude": 37.71801888888889,
                    "maxLongitude": -121.46994805555556,
                    "maxLatitude": 37.72300888888889
                }
            },
            "tripDetails": {
                "electricalConsumption": True,
                "electricalRegeneration": True,
                "fuelConsumption": True,
                "distance": 6115,
                "startOdometer": 2686000,
                "startTime": "2023-08-05T18:59:42+0000",
                "startPosition": {
                    "latitude": 37.71815083333333,
                    "longitude": -121.46994805555556,
                    "address": "Perry Ln 2939, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "endOdometer": 2692000,
                "endTime": "2023-08-05T19:11:08+0000",
                "endPosition": {
                    "latitude": 37.72277611111111,
                    "longitude": -121.53198583333334,
                    "address": "International Pkwy 25441, 95377 Tracy, United States",
                    "postalCode": "95377",
                    "city": "Tracy",
                    "region": "CA",
                    "country": "United States"
                },
                "totalEcoScore": {
                    "score": 98.0,
                    "scoreStatus": "VALID"
                },
                "throttleEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "speedEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "brakeEcoScore": {
                    "score": 4.9,
                    "scoreStatus": "VALID"
                },
                "averageSpeed": 30.577536000000002,
                "averageFuelConsumption": 21.0013020611415,
                "averageEnergyConsumption": 0.0,
                "energyRegenerated": 0.0,
                "averagePHEVFuelConsumption": True,
                "evDistance": 0.0
            }
        }
    ]
}

for i in trips["trips"]:#[38:39]:
    #print(i)
    print(i['id'])
    print(i['routeDetails'])
    print(i['tripDetails']['startPosition']['address'])
    print(i['tripDetails']['endPosition']['address'])
    print(i['tripDetails']['startOdometer'])
    print(i['tripDetails']['endOdometer'])
    print(i['tripDetails']['averageSpeed'])
    print(i['tripDetails']['averageFuelConsumption']) '''


c = jlrpy.Connection('sjpbailey@comcast.net', 'password')
# c = jlrpy.Connection(email='sjpbailey@comcast.net',
#                    refresh_token='124c3f21-42ds-2e4d-86f8-221v32392a1d')

v = c.vehicles[0]
print(v)
c = c.get_user_info()
print(c)
