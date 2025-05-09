from typing_extensions import Annotated

# Metadata added to specify units


def calculate_distance(speed: Annotated[int, 'km/h'], time: Annotated[int, 'hours']) -> int:
    return speed * time
