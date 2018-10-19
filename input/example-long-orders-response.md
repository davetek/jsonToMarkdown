{ 
  "eventType":"ORDERS.TRANSPORTATION.CREATED",
  "resource":"https://integration1.api.manheim.com/orders/pickup/id/dc6b823a-3a41-11e7-b8b1-2b8e9280aa11",
  "body":{ 
    "type":"ORDERS.TRANSPORTATION.PICKUP",
    "status":"REQUESTED",
    "unit":{ 
      "href":"https://integration1.api.manheim.com/units/id/eb227e5c-398b-11e7-a83f-05f75decaa11",
      "type":"Passenger Vehicle",
      "vin":"2CNDL63F956059926",
      "operable":true,
      "owner":{ 
        "href":"https://integration1.api.manheim.com/contacts/id/430c66e3-e57e-4399-9bcf-52140376aa11/company",
        "customerName":"John Smith Cars",
        "alternativeIDs":[ 
          { 
            "type":"AA",
            "value":"1234567"
          }
        ],
        "dealershipType":"Dealer"
      },
      "title":{ 

      },
      "consignment":{ 
        "href":"https://integration1.api.manheim.com/consignments/id/831a0738-3a37-11e7-a623-7979e72aa11",
        "referenceId":{ 
          "workOrder":"1111111"
        },
        "operatingLocation":{ 
          "href":"https://integration1.api.manheim.com/locations/id/AAA"
        },
        "createdOn":"2017-05-16T12:59:35.525Z"
      },
      "odometer":{ 
        "digits":0,
        "reading":0,
        "type":"DIGITAL",
        "units":"MILES"
      },
      "description":{ 
        "modelYear":2005,
        "make":"Chevrolet",
        "model":"Equinox",
        "trim":"LT",
        "interiorColor":{ 
          "description":"Bei"
        },
        "exteriorColor":{ 
          "description":"Beige"
        },
        "engine":{ 
          "type":"V6 Cylinder Engine",
          "horsepower":185,
          "displacement":3.4,
          "fuelType":"Gasoline Fuel"
        },
        "transmission":"5-Speed A/T"
      },
      "account":{ 
        "href":"https://integration1.api.manheim.com/contacts/id/430c66e3-e57e-4399-9bcf-5214037aa111/account",
        "customer":{ 
          "href":"https://integration1.api.manheim.com/contacts/id/430c66e3-e57e-4399-9bcf-5214037aa111/company"
        }
      }
    },
    "createdOn":"2017-05-16T14:13:40.341+00:00",
    "updatedOn":"2017-05-16T14:13:40.341+00:00",
    "transporter":"Transports Cars",
    "verifiedAvailableForTransport":true,
    "hasKeys":true,
    "inventorySource":"Regular",
    "onHold":false,
    "chargesDueTransporter":75.0,
    "pickupLocation":{ 
      "name":"John Smith Cars",
      "address1":"123 Main Lane",
      "city":"Atlanta",
      "stateProvinceCode":"GA",
      "countryCode":"US",
      "zipcode":"30328"
    },
    "pickupContacts":[ 
      { 
        "number":"5555555555"
      }
    ],
    "deliveryLocation":{ 
      "type":"AUCTION",
      "name":"Manheim Atlanta",
      "address1":"4900 Buffington Rd",
      "city":"Atlanta",
      "stateProvinceCode":"GA",
      "countryCode":"US",
      "zipcode":"30349"
    },
    "deliveryContacts":[ 
      { 
        "name":"MICHELLE"
      }
    ],
    "href":"https://integration1.api.manheim.com/orders/pickup/id/dc6b823a-3a41-11e7-b8b1-2b8e9280aa11"
  },
  "relatedResources":[ 
    "https://integration1.api.manheim.com/companies/id/1111111",
    "https://integration1.api.manheim.com/accounts/id/1111111"
  ]
}