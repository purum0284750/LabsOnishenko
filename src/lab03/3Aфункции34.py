text2 = ["bb","aa","bb","aa","cc"]


def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {}
    for token in tokens:
        result[token] = result.get(token, 0) + 1
    return result


text3 = count_freq(text2)


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    result = []
    for key in freq:
        value = freq[key]
        element = (key, value)
        result.append(element)


    result = sorted(result, key=lambda p: p[0])[:n]

    return result


text4 = top_n(text3)
print(text4)
