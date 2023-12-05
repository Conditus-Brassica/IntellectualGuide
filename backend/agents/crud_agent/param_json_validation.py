"""
get_categories_of_region
"""
get_categories_of_region_json = \
    {
        "type": "object",
        "properties": {
            "region_name": {"type": "string"},
            "optional_limit": {"type": ["number", "null"]}
        },
        "required": ["region_name"],
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_landmarks_in_map_sectors
"""
get_landmarks_in_map_sectors_json = \
    {
        "type": "object",
        "properties": {
            "map_sectors_names":
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "additionalProperties": False
                },
            "optional_limit": {"type": ["number", "null"]},
            "additionalProperties": False
        },
        "required": ["map_sectors_names"],
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_landmarks_refers_to_categories
"""
get_landmarks_refers_to_categories_json = \
    {
        "type": "object",
        "properties": {
            "categories_names":
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "additionalProperties": False
                },
            "optional_limit": {"type": ["number", "null"]},
            "additionalProperties": False
        },
        "required": ["categories_names"],
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_landmarks_by_coordinates
"""
get_landmarks_by_coordinates_json = \
    {
        "type": "object",
        "properties": {
            "coordinates": {
                "type": "array",
                "items":
                    {
                        "type": "object",
                        "properties": {
                            "latitude": {"type": "number"},
                            "longitude": {"type": "number"}
                        },
                        "required": ["latitude", "longitude"],
                        "maxProperties": 2,
                        "additionalProperties": False
                    },
                "additionalProperties": False
            },
            "optional_limit": {"type": ["number", "null"]}
        },
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_landmarks_by_names
"""
get_landmarks_by_names_json = \
    {
        "type": "object",
        "properties": {
            "landmark_names":
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "additionalProperties": False
                },
            "optional_limit": {"type": ["number", "null"]},
            "additionalProperties": False
        },
        "required": ["landmark_names"],
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_landmarks_of_categories_in_region
"""
get_landmarks_of_categories_in_region_json = \
    {
        "type": "object",
        "properties": {
            "region_name":
                {
                    "type": "string"
                },
            "categories_names":
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                },
            "optional_limit": {"type": ["number", "null"]}
        },
        "required": ["categories_names", "region_name"],
        "maxProperties": 3,
        "additionalProperties": False
    }

"""
get_landmarks_by_region
"""
# Он такой же как и у get_categories_of_region_json
get_landmarks_by_region_json = \
    {
        "type": "object",
        "properties": {
            "region_name": {"type": "string"},
            "optional_limit": {"type": ["number", "null"]}
        },
        "required": ["region_name"],
        "maxProperties": 2,
        "additionalProperties": False
    }

"""
get_recommendations_for_landmark_by_region
"""
get_recommendations_for_landmark_by_region_json = \
    {
        "type": "object",
        "properties": {
            "user_login": {"type": "string"},
            "current_latitude": {"type": "number"},
            "current_longitude": {"type": "number"},
            "current_name": {"type": "string"},
            "amount_of_recommendations": {"type": "number"}

        },
        "required": ["user_login", "current_latitude", "current_longitude", "current_name",
                     "amount_of_recommendations"],
        "maxProperties": 5,
        "additionalProperties": False
    }
