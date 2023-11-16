"""
Schema for checking sectors from client.
"""
sector_schema_receive = {
    "type": "object",
    "properties": {
        "tl_lat": {"type": "number"},
        "tl_lng": {"type": "number"},
        "br_lat": {"type": "number"},
        "br_lng": {"type": "number"}
    },
    "required": ["tl_lat", "tl_lng", "br_lat", "br_lng"],
    "additionalProperties": False
}

"""
Schema for sending sector request to client.
"""
sector_send_schema = {
    "type": "object",
    "properties": {"points": {
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
    }
}

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

"""
Schema for sending one point.
"""
send_point = {
    "type": "object",
    "properties": {
        "name": "string",
        "lat": "number",
        "lng": "number",
        "cat": "string"
    },
    "required": ["name", "lat", "lng", "cat"],
    "additionalProperties": False
}
