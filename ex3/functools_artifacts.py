from functools import reduce, partial, lru_cache, singledispatch
import operator
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case '/':
            return reduce(operator.floordiv, spells)
        case '+':
            return reduce(operator.add, spells)
        case '-':
            return reduce(operator.sub, spells)
        case '*':
            return reduce(operator.mul, spells)
        case _:
            raise ValueError('Unsupported operation')


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 'fire', 50),
        'ice_enchant': partial(base_enchantment, 'ice', 50),
        'lightning_enchant': partial(base_enchantment, 'lightning', 50)
    }


def non_memoized_fibonacci(n: int) -> int:
    if (n < 2):
        return n
    return (non_memoized_fibonacci(n - 1) + non_memoized_fibonacci(n - 2))


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if (n < 2):
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(arg: any) -> str:
        raise NotImplementedError('Unsupported type')

    cast_spell.register(
        str,
        lambda arg: 'Enchanting ' + arg
    )
    cast_spell.register(
        int,
        lambda arg: 'Casting spell with power ' + str(arg)
    )
    cast_spell.register(
        list,
        lambda arg: 'Combining spells with powers ' + str(arg)
    )

    return cast_spell


def main() -> None:
    # use of reduce
    spells = [10, 5, 2]
    print('Testing spell reducer:')
    print(f'Addition: {spell_reducer(spells, "+")}')
    print(f'Multiplication: {spell_reducer(spells, "*")}')

    # use of partial
    def base_enchantment(enchantment_type: str, power: int, name: str) -> str:
        return f'{name} with {enchantment_type} enchantment and power {power}'
    print('\nTesting partial enchanter:')
    enchanter = partial_enchanter(base_enchantment)
    print(enchanter['fire_enchant']('sword'))
    print(enchanter['ice_enchant']('shield'))

    # use of lru_cache
    print('\nTesting Fibonacci functions:')
    n = 30
    start_time = time.time()
    print(f'Non-memoized Fibonacci of {n}: {non_memoized_fibonacci(n)}')
    print(f'Time taken: {time.time() - start_time:.4f} seconds')

    start_time = time.time()
    print(f'Memoized Fibonacci of {n}: {memoized_fibonacci(n)}')
    print(f'Time taken: {time.time() - start_time:.4f} seconds')

    # use of singledispatch
    print('\nTesting spell dispatcher:')
    dispatcher = spell_dispatcher()
    print(dispatcher('fireball'))
    print(dispatcher(100))
    print(dispatcher([10, 20, 30]))


if __name__ == '__main__':
    main()
