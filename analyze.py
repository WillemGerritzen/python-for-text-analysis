from utils import get_paths, get_basic_stats

paths = get_paths('Data/books')

book2stats = {}

for file in paths:
    stat = get_basic_stats(file)
    print(stat)
    book2stats[file.strip('.txt')] = stat

print(book2stats)

stats2book_with_highest_value = {}

tmp_lst = []

for stat in list(list(book2stats.values())[0].keys()):
    for title in range(len(book2stats)):
        tmp_lst.append(list(book2stats.values())[title][stat])
        if len(tmp_lst) >= len(book2stats):
            stats2book_with_highest_value[stat] = list(book2stats.keys())[tmp_lst.index(sorted(tmp_lst)[-1])]
            tmp_lst.clear()
            break

print(stats2book_with_highest_value)


