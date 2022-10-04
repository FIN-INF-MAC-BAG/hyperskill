def match(string, r):
    if not r or (r == '$' and not string):
        return True
    if not string and r:
        return False
    if len(r) > 1:
        if r[0] == '\\':
            return match(string[1:], r[2:])
        if r[1] == '?':
            return match(string, r.replace('?', '')) or match(string, r[2:])
        if r[1] == '*':
            return match(string, r[2:]) or match(string[1:], r)
        if r[1] == '+':
            return match(string, r.replace('+', '')) or match(string[1:], r)
    return match(string[1:], r[1:]) if r[0] == string[0] or r[0] == '.' else False


def compare_length(string, r):
    if match(string, r):
        return True
    if r and r[0] == '^':
        return match(string, r.replace('^', ''))
    elif string:
        return compare_length(string[1:], r)
    return False


regex, word = input().split('|')
print(compare_length(word, regex))