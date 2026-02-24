def spell(value: str) -> None:
    print(f"Casting spell {value}...")


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda: (spell1('1'), spell2('2'))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: [base_spell(str(i)) for i in range(multiplier)]


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda: (spell('true') if condition() else None)


def spell_sequence(spells: list[callable]) -> callable:
    return lambda: [spell(i) for i, spell in enumerate(spells)]


def main() -> None:
    print("Testing spell combiner:")
    combined_spell = spell_combiner(spell, spell)
    combined_spell()

    print("\nTesting power amplifier:")
    amplified_spell = power_amplifier(spell, 3)
    amplified_spell()

    print("\nTesting conditional caster:")
    condition_true: callable = lambda: True
    condition_false: callable = lambda: False
    conditional_spell_true = conditional_caster(condition_true, spell)
    conditional_spell_false = conditional_caster(condition_false, spell)
    conditional_spell_true()
    conditional_spell_false()

    print("\nTesting spell sequence:")
    sequence_spell = spell_sequence([spell, spell, spell])
    sequence_spell()


if __name__ == '__main__':
    main()
