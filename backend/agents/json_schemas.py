import json

"""
Schema for checking sectors from client.
"""
sector_schema_receive = '''{
    "type": "object",
    "properties": {
        "TL": {
            "type": "object",
            "properties": {
                "lat": {
                    "type": "number"
                },
                "lng": {
                    "type": "number"
                }
            },
            "required": ["lat", "lng"]
        },
        "BR": {
            "type": "object",
            "properties": {
                "lat": {
                    "type": "number"
                },
                "lng": {
                    "type": "number"
                }
            },
            "required": ["lat", "lng"],
            "additionalProperties": False
        }
    },
    "required": ["TL", "BR"],
    "additionalProperties": False
}'''

"""
Schema for sending sector request to client.
"""
sector_send_schema = '''{
    "type": "array",
    "items":
        {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "lat": {
                    "type": "number"
                },
                "lng": {
                    "type": "number"
                },
                "cat": {
                    "type": "string"
                }
            },
            "required": ["name", "lat", "lng", "cat"],
            "additionalProperties": False
        }
}'''


"""
Schema for checking sending route points.
"""
send_rout_schema = ''''{
    "type": "array",
    "items":
        {
            "type": "object",
            "properties": {
                "lat": {
                    "type": "number"
                },
                "lng": {
                    "type": "number"
                },
            },
            "required": ["lat", "lng"],
            "additionalProperties": false
        }
}'''
