"""
get_coords_of_map_sectors
"""
get_coords_of_map_sectors_json = \
    {
        "type": "object",
        "properties": {
            "TL": {
                "type": "object",
                "properties": {
                    "latitude": {
                        "latitude": "number"
                    },
                    "longitude": {
                        "type": "number"
                    },
                },
                "required": ["latitude", "longitude"],
                "maxProperties": 2,
                "additionalProperties": False
            },
            "BR": {
                "type": "object",
                "properties": {
                    "latitude": {
                        "latitude": "number"
                    },
                    "longitude": {
                        "type": "number"
                    },
                },
                "required": ["latitude", "longitude"],
                "maxProperties": 2,
                "additionalProperties": False
            }
        },
        "required": ["TL", "BR"],
        "maxProperties": 2,
        "additionalProperties": False
    }
