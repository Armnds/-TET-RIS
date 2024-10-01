import itertools

items = [4, 8, 1, 3, 4, 2, 6, 3, 4, 5, 9, 3, 3, 5, 2, 3]
bin_capacity = 30

# Generate all subsets of the items
all_subsets = []
for r in range(len(items) + 1):
    subsets_r = list(itertools.combinations(items, r))
    all_subsets.extend(subsets_r)

print(all_subsets)  # This will print all possible subsets of items


# Initialize the best subset
best_subset = None
best_sum = 0

for subset in all_subsets:
    total_size = sum(subset)
    if total_size <= bin_capacity and total_size > best_sum:
        best_subset = subset
        best_sum = total_size

print(f"Best Subset: {best_subset} with size {best_sum}")
