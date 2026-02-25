from functools import wraps
from random import random


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict[str, any]) -> any:
        print(f"Starting to cast {args[1]}...")
        result = func(*args, **kwargs)
        print(f"Finished casting {args[1]}!")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict[str, any]) -> any:
            power = args[2]
            if power < min_power:
                raise ValueError(f"Power must be at least {min_power}.")
            return func(*args, **kwargs)
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict[str, any]) -> any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed: {e}")
                    attempts += 1
            raise Exception(f"Failed to cast spell after {max_attempts} "
                            "attempts.")
        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not name.isalpha() and len(name) < 3:
            raise ValueError("Mage name must be at least 3 characters long "
                             "and contain only letters.")

    @spell_timer
    @power_validator(min_power=10)
    @retry_spell(max_attempts=3)
    def cast_spell(self, spell_name: str, power: int) -> str:
        random_chance = random()
        if random_chance < 0.7:
            raise Exception("Spell failed due to magical interference.")
        return f'Successfully {spell_name} with power {power}!'


def main() -> None:
    mage = MageGuild()
    try:
        MageGuild.validate_mage_name("Gandalf")
        print(mage.cast_spell("Fireball", 12))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
