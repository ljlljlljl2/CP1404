"""
Wimbledon
Estimate: 35 minutes
Actual:   45 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = read_wimbledon_data(FILENAME)
    champion_to_wins = count_champion_wins(records)
    countries = get_champion_countries(records)
    display_results(champion_to_wins, countries)


def read_wimbledon_data(filename):
    """Read Wimbledon data from file and return records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champion_wins(records):
    """Return dictionary of champion names to number of wins."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_champion_countries(records):
    """Return sorted set of champion countries."""
    countries = set()
    for record in records:
        countries.add(record[1])
    return sorted(countries)


def display_results(champion_to_wins, countries):
    """Display Wimbledon champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()