from sets_of_pencils import pencils

print(pencils)

pencils_needed = set({'6H', '5H', '4H', '3H', '2H', 'H', 'F', 'HB', 'B', '2B', '3B', '4B', '5B', '6B'})

final_pencil_sets = set()

while pencils_needed:
    best_set = None
    pencil_hardness_covered = set()
    for pencil_set, hardness_in_set in pencils.items():
        covered = pencils_needed & hardness_in_set
        if len(covered) > len(pencil_hardness_covered):
            best_set = pencil_set
            pencil_hardness_covered = covered
    pencils_needed -= pencil_hardness_covered
    final_pencil_sets.add(best_set)

print(final_pencil_sets)

print(pencils['orion'] | pencils['tintenstift'] | pencils['pobeda'] | pencils['taifun'])
