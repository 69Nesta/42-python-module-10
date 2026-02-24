def mage_counter() -> callable:
    counter: int = 0

    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter

    return increment


def spell_accumulator(initial_power: int) -> callable:
    spell_power: int = initial_power

    def accumulate(power: int) -> int:
        nonlocal spell_power
        spell_power += power
        return spell_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def create_enchantment(item: str) -> str:
        return f'{enchantment_type} {item}'

    return create_enchantment


def memory_vault() -> dict[str, callable]:
    vault: dict[str, any] = {}

    def store(key: str, value: any) -> None:
        vault.update({key: value})

    def recall(key: str) -> any:
        return vault.get(key, 'Memory not found')

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print('Testing mage counter:')
    counter = mage_counter()
    for i in range(5):
        print(f'Call {i}: {counter()}')

    print('\nTesting spell accumulator:')
    accumulator = spell_accumulator(10)
    print(accumulator(0))
    print(accumulator(5))

    print('\nTesting enchantment factory:')
    fire_enchantment = enchantment_factory('fire')
    ice_enchantment = enchantment_factory('ice')
    print(fire_enchantment('sword'))
    print(ice_enchantment('shield'))

    print('\nTesting memory vault:')
    vault = memory_vault()
    vault['store']('hello', 'world')
    print(vault['recall']('hello'))
    print(vault['recall']('world'))


if __name__ == '__main__':
    main()
