import os
import sys
from collections import defaultdict

floor = int

class Rule:
    def __init__(self, first, second):
        self.first = int(first)
        self.second = int(second)

    def __repr__(self):
        return f"{self.first}|{self.second}"

def filter_rules(rules, update):
    return filter(lambda rule: rule.first in update and rule.second in update, rules)

with open(sys.argv[1], "r") as f:
    puzzle = f.read()
    rules = []
    for rule in puzzle.split("\n\n")[0].split("\n"):
        rules.append(Rule(rule.split("|")[0], rule.split("|")[1]))

    updates = []
    for update in puzzle.split("\n\n")[1].split("\n"):
        if update == '':
            continue
        updates.append([int(u) for u in update.split(',')])

    sorted_updates = []
    for update in updates:
        filtered_rules = list(filter_rules(rules, update))
        counts = defaultdict(lambda: 0, {})
        for rule in filtered_rules:
            counts[rule.first] += 1
        sorted_update =sorted(counts.items(), key=lambda k: k[1], reverse=True)
        ordered = [s[0] for s in sorted_update]
        sorted_updates.append(ordered)

    new = []
    for su in sorted_updates:
        new.append(su)

    total = 0
    incorrect_total = 0
    for update, sorted_update in zip(updates, new):
        if update[:-1] == sorted_update:
            total += update[(len(update)//2)]
        else:
            incorrect_total += sorted_update[(len(sorted_update)//2)]

    print(total)
    print(incorrect_total)
