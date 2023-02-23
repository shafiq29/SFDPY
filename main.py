# Author    : Shafiqul Islam <shafiqrobin9@gmail.com>
# Date      : 23-02-2023

import json
from simple_salesforce import SalesforceLogin, Salesforce

# credentials are set here
loginInfo       = json.load(open("login-mock.json"))
username        = loginInfo["username"]
password        = loginInfo["password"]
security_token  = loginInfo["security_token"]
domain          = loginInfo["domain"]

# login to salesforce
session_id, instance = SalesforceLogin(
    username=username, 
    password=password, 
    security_token=security_token, 
    domain=domain
)
sf = Salesforce(
    instance=instance, 
    session_id=session_id
)

# let us create custom objects first using metadata api
mdapi = sf.mdapi

custom_objects = [
    mdapi.CustomObject(
        fullName="MyCustomObject1__c",
        label="My Custom Object 1",
        pluralLabel="My Custom Objects 1",
        nameField=mdapi.CustomField(label="Name", type=mdapi.FieldType("Text")),
        deploymentStatus=mdapi.DeploymentStatus("Deployed"),
        sharingModel=mdapi.SharingModel("Read"),
    ),
    mdapi.CustomObject(
        fullName="MyCustomObject2__c",
        label="My Custom Object 2",
        pluralLabel="My Custom Objects 2",
        nameField=mdapi.CustomField(label="Name", type=mdapi.FieldType("Text")),
        deploymentStatus=mdapi.DeploymentStatus("Deployed"),
        sharingModel=mdapi.SharingModel("Read"),
    ),
    # add more custom objects here as per need
]

for custom_object in custom_objects:
    mdapi.CustomObject.create(custom_object)

# now let us create custom fields using tooling api
url = 'tooling/sobjects/CustomField/'

# replace with your object name
object_api_name = 'MyCustomObject1__c'

fields_data = [
    {
        'api_name': 'MyCustomField1__c',
        'label': 'My Custom Field 1',
        'data_type': 'Text',
        'length': 100,
        'required': False,
        'inline_help_text': 'This is custom field 1'
    },
    {
        'api_name': 'MyCustomField2__c',
        'label': 'My Custom Field 2',
        'data_type': 'Number',
        'precision': 10,
        'scale': 2,
        'required': True,
        'inline_help_text': 'This is custom field 2'
    }
]

# in loop create custom fields

for field_data in fields_data:
    payload = {
        'Metadata': {
            'type': field_data['data_type'],
            'inlineHelpText': field_data['inline_help_text'],
            'precision': field_data.get('precision'),
            'scale': field_data.get('scale'),
            'label': field_data['label'],
            'length': field_data.get('length'),
            'required': field_data['required']
        },
        'FullName': f"{object_api_name}.{field_data['api_name']}"
    }
    result = sf.restful(url, method='POST', json=payload)
