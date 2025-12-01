def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:n]


example_count_freq = ["bb", "aa", "bb", "aa", "cc"]
res_count_freq = count_freq(example_count_freq)
res_count_top_n = top_n(res_count_freq)
print(res_count_freq)
print(res_count_top_n)
