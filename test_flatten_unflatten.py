import copy

from flat_dictionary import flat_nested_dict, unflatten_dict  # change module name


def test_flatten_simple_dict():
    data = {"a": 1, "b": 2}
    expected = {"a": 1, "b": 2}
    assert flat_nested_dict(data) == expected


def test_flatten_nested_dict():
    data = {
        "user": {
            "id": 1034,
            "profile": {
                "name": "Sanidhya",
                "contacts": {
                    "email": "sanidhya@example.com",
                    "phone": {"primary": "+91...", "alternate": None},
                },
            },
        }
    }

    flattened = flat_nested_dict(data)

    assert flattened["user.id"] == 1034
    assert flattened["user.profile.name"] == "Sanidhya"
    assert flattened["user.profile.contacts.email"] == "sanidhya@example.com"
    assert flattened["user.profile.contacts.phone.primary"].startswith("+91")
    assert "user.profile.contacts.phone.alternate" in flattened


def test_flatten_preserves_lists_as_values():
    data = {
        "user": {
            "skills": ["Python", "React", "FastAPI"],
        }
    }

    flattened = flat_nested_dict(data)

    assert flattened == {
        "user.skills": ["Python", "React", "FastAPI"],
    }


def test_unflatten_simple_dict():
    flat = {"a": 1, "b": 2}
    expected = {"a": 1, "b": 2}
    assert unflatten_dict(flat) == expected


def test_unflatten_nested_dict():
    flat = {
        "user.id": 1034,
        "user.profile.name": "Sanidhya",
        "user.profile.contacts.email": "sanidhya@example.com",
    }

    result = unflatten_dict(flat)

    assert result["user"]["id"] == 1034
    assert result["user"]["profile"]["name"] == "Sanidhya"
    assert result["user"]["profile"]["contacts"]["email"] == "sanidhya@example.com"


def test_roundtrip_flatten_then_unflatten():
    original = {
        "user": {
            "id": 1034,
            "profile": {
                "name": "Sanidhya",
                "skills": ["Python", "React"],
            },
        },
        "meta": {"region": "Asia", "active": True},
    }

    flattened = flat_nested_dict(original)
    restored = unflatten_dict(flattened)

    assert restored == original


def test_roundtrip_unflatten_then_flatten():
    flat = {
        "a.b.c": 1,
        "a.b.d": 2,
        "x": 3,
    }

    nested = unflatten_dict(flat)
    flattened_again = flat_nested_dict(nested)

    assert flattened_again == flat


def test_custom_separator_roundtrip():
    original = {"a": {"b": {"c": 1}}}
    sep = "__"

    flattened = flat_nested_dict(original, separator=sep)
    assert flattened == {"a__b__c": 1}

    restored = unflatten_dict(flattened, separator=sep)
    assert restored == original


def test_flatten_does_not_mutate_input():
    original = {
        "user": {"id": 1, "profile": {"name": "Test"}},
    }
    snapshot = copy.deepcopy(original)

    _ = flat_nested_dict(original)

    assert original == snapshot
