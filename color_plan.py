def color_plan(n, m):
    if n > m:
        return "impossible"
    if m >= n:
        temp_m = m
        result = 1
        for _ in range(n):
            result *= temp_m
            temp_m -= 1
        return result

    if n == 1:
        return m
    return m * (m - 1) ** (n - 1) - question1(n - 1, m)


print(color_plan(2, 2))
