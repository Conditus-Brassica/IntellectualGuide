"""
Schema for checking sectors from client.
"""
sector_schema_receive = {
    "type": "object",
    "properties": {
        "tl_lat": "number",
        "tl_lng": "number",
        "br_lat": "number",
        "br_lng": "number"
    },
    "required": ["tl_lat", "tl_lng", "br_lat", "br_lng"],
    "additionalProperties": False
}

"""
Schema for sending sector request to client.
"""
sector_send_schema = {
    "type": "object",
    "properties": {"points":
        {
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
        }, "required": ["points"],
        "additionalProperties": False
    }}

"""
Schema for checking sending route points.
"""
send_rout_schema = {
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
            "additionalProperties": False
        }
}
