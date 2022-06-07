from faunadb import query as q
from fauna import get_fauna_client


def create_collection(client, config):
    if "name" not in config:
        raise ValueError("Missing collection name.")
    client.query(
        q.if_(
            q.exists(q.collection(config["name"])),
            {},
            q.create_collection(config)
        )
    )


def create_index(client, config):
    if "name" not in config:
        raise ValueError("Missing index name.")
    if "source" not in config:
        raise ValueError("Missing index source.")
    r = client.query(
        q.if_(
            q.exists(q.index(config["name"])),
            {},
            q.create_index(config)
        )
    )


def main():
    client = get_fauna_client()
    create_collection(client, {"name": "houses"})
    create_index(client, {"name": "all_houses", "source": q.collection("houses")})

    # Delete all previous houses
    client.query(
        q.map_(
            q.lambda_query(lambda x: q.delete(x)),
            q.paginate(q.match(q.index("all_houses")), 100000)
        )
    )

    client.query(q.create(q.collection("houses"), {
        "data": {
            "street": "Time Square",
            "city": "New York",
            "rooms": [
                {"name": "Kitchen", "area": 20, "wall_color": "white"},
                {"name": "Living Room", "area": 40, "wall_color": "yellow"},
                {"name": "Bedroom", "area": 30, "wall_color": "red"},
            ],
        }
    }))

    client.query(q.create(q.collection("houses"), {
        "data": {
            "street": "Rue de la paix",
            "city": "Paris",
            "rooms": [
                {"name": "Kitchen", "area": 10, "wall_color": "white"},
                {"name": "Living Room", "area": 20, "wall_color": "yellow"},
                {"name": "Bedroom", "area": 10, "wall_color": "red"},
                {"name": "Bedroom", "area": 10, "wall_color": "green"},
            ],
        }
    }))

    client.query(q.create(q.collection("houses"), {
        "data": {
            "street": "Alexanderplatz",
            "city": "Berlin",
            "rooms": [
                {"name": "Kitchen", "area": 30, "wall_color": "white"},
                {"name": "Living Room", "area": 40, "wall_color": "yellow"},
                {"name": "Bedroom", "area": 10, "wall_color": "orange"},
                {"name": "Bedroom", "area": 10, "wall_color": "green"},
                {"name": "Bedroom", "area": 12, "wall_color": "white"},
            ],
        }
    }))







if __name__ == '__main__':
    main()
