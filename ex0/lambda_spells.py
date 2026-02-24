# Lambda Sanctum Test Data
ARTIFACTS = [
    {'name': 'Light Prism', 'power': 86, 'type': 'relic'},
    {'name': 'Earth Shield', 'power': 80, 'type': 'relic'},
    {'name': 'Fire Staff', 'power': 117, 'type': 'relic'},
    {'name': 'Storm Crown', 'power': 77, 'type': 'weapon'}
]

MAGES = [
    {'name': 'Storm', 'power': 81, 'element': 'earth'},
    {'name': 'Rowan', 'power': 54, 'element': 'earth'},
    {'name': 'Zara', 'power': 98, 'element': 'shadow'},
    {'name': 'Kai', 'power': 92, 'element': 'water'},
    {'name': 'Ember', 'power': 53, 'element': 'ice'}
]

SPELLS = ['meteor', 'heal', 'shield', 'earthquake']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact.get('power', 0),
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda mage: mage.get('power') >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda spell: f'* {spell} *', spells)


def mage_stats(mages: list[dict]) -> dict:
    mages_power = [mage.get('power') for mage in mages]
    return {
        'max_power': max(mages_power),
        'min_power': min(mages_power),
        'avg_power': sum(mages_power) / len(mages_power)
    }


def main() -> None:
    print("Artifacts sorted by power (desc):")
    sorted_artifacts = artifact_sorter(ARTIFACTS)
    for art in sorted_artifacts:
        print(" - {} (power={}, type={})".format(
            art.get('name'), art.get('power'), art.get('type')
        ))
    print()

    min_power = 80
    print(f"Mages with power >= {min_power}:")
    strong_mages = power_filter(MAGES, min_power)
    for mage in strong_mages:
        print(" - {} (power={}, element={})".format(
            mage.get('name'), mage.get('power'), mage.get('element')
        ))
    print()

    print("Transformed spells:")
    transformed = spell_transformer(SPELLS)
    for s in transformed:
        print(f" - '{s}'")
    print()

    print("Mage stats:")
    stats = mage_stats(MAGES)
    print(f" - max_power: {stats.get('max_power')}")
    print(f" - min_power: {stats.get('min_power')}")
    print(f" - avg_power: {stats.get('avg_power')}")


if __name__ == '__main__':
    main()
