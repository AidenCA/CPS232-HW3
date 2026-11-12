def sort_seven(x1, x2, x3, x4, x5, x6, x7):
    comparisons = 0

    # The given relationships already tell us x1 is the largest.
    result = [x1]
    print(f"Start with x1 = {x1}. No comparison needed.")

    # x2 is already first in Group A. Compare its other two numbers.
    comparisons += 1
    if x4 >= x5:
        group_a = [x2, x4, x5]
    else:
        group_a = [x2, x5, x4]
    print(f"Comparison {comparisons}: {x4} vs. {x5} -> Group A: {group_a}")

    # x3 is already first in Group B. Compare its other two numbers.
    comparisons += 1
    if x6 >= x7:
        group_b = [x3, x6, x7]
    else:
        group_b = [x3, x7, x6]
    print(f"Comparison {comparisons}: {x6} vs. {x7} -> Group B: {group_b}")

    # i and j point to the first unused number in each group.
    i = 0
    j = 0

    print("\nMerging the groups:")
    while i < len(group_a) and j < len(group_b):
        a = group_a[i]
        b = group_b[j]
        comparisons += 1

        # Add the larger number and move forward in its group.
        if a >= b:
            chosen = a
            i += 1
        else:
            chosen = b
            j += 1

        result.append(chosen)
        print(f"Comparison {comparisons}: {a} vs. {b} -> Add {chosen}. List: {result}")

    # One group has run out. The remaining numbers are already sorted.
    remaining = group_a[i:] + group_b[j:]
    result.extend(remaining)
    print(f"Add the remaining numbers {remaining} without comparing them.")
    print(f"Total comparisons: {comparisons}")

    return result


# Run the function and print the final sorted list.
# This input shows the worst case of exactly 7 comparisons.
sorted_numbers = sort_seven(7, 6, 5, 4, 2, 3, 1)
print(f"Sorted list: {sorted_numbers}")

# Count the possible orders for seven distinct numbers.
# x1 is fixed at the front, and each group has 2 possible orders.
# Choosing 3 of the 6 remaining positions for Group A gives 20 ways
# to mix the groups. Group B fills the other 3 positions.
possible_orders = 2 * 2 * 20

print(f"Possible orders: 2 * 2 * 20 = {possible_orders}")
print("Six comparisons can distinguish at most 2**6 = 64 orders.")
print("Since 64 < 80, the worst-case lower bound is 7 comparisons.\n")
