def duplicates(list):
    frequency = {}
    duplicates = []
    unique = []

    # Count the frequency of each element
    for num in list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

#for separating duplicates
    for num, count in frequency.items():
        if count > 1:
            duplicates.append(num)
        else:
            unique.append(num)

    return duplicates, unique

# Example:
a = [1, 5, 1, 3, 7, 21, 25, 2, 5, 3, 21]
duplicates, unique = duplicates(a)

print("List-1 -", sorted(duplicates))
print("List-2 -", sorted(unique))