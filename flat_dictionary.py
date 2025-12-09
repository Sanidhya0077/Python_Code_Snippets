nested_dict = {
    "user": {
        "id": 1034,
        "profile": {
            "name": "Sanidhya",
            "contacts": {
                "email": "sanidhya@example.com",
                "phone": {
                    "primary": "+91 9876543210",
                    "alternate": None
                }
            },
            "skills": ["Python", "React", "FastAPI"]
        }
    },
    "account": {
        "type": "premium",
        "status": "active",
        "usage": {
            "current_month": {
                "messages": 143,
                "storage_mb": 512.45,
                "features_enabled": {
                    "ai_chat": True,
                    "analytics": True,
                    "priority_support": False
                }
            },
            "history": {
                "months": {
                    "oct": {"messages": 98, "storage_mb": 304.12},
                    "nov": {"messages": 120, "storage_mb": 450.50}
                }
            }
        }
    },
    "meta": {
        "created_at": "2024-11-02",
        "region": "Asia",
        "tags": ["test", "sample", "flatten"]
    }
}

# define a flat function
def flat_nested_dict(nested_dict,parent_key="", separator="."):
    items = {} 
    for key,value in nested_dict.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value,dict):
            items.update(flat_nested_dict(value,separator=".",parent_key=key))
            # if value is of type dictionary then call the function recursively again
        else:
            items[new_key] = value
    return items

print(flat_nested_dict(nested_dict))

def unflatten_dict(nested_dict, separator="."):
    result = {}

    for flat_key, value in flat_nested_dict(nested_dict).items():
        keys = flat_key.split(separator)
        d = result

        for key in keys[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]

        d[keys[-1]] = value

    return result

print(unflatten_dict(flat_nested_dict(nested_dict)))