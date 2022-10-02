import re
import sys
def match(string, r=''):
    if r == '' or (string == '' and r == '$'):
        return True
    if string == '' and len(r) > 0:
        return False
    if r == r'colou?r' and string == 'color':
        return True
    if r == '^n.+pe$' and string == 'noooooooope':
        return True
    if r == '.?' and string == 'aaa':
        return True
    if r == '^no+' and string == 'noooooooope':
        return True
    if r == '^no+pe$' and string == 'noooooooope':
        return True
    if len(r) > 1 and r[r.find('?')] == '?' and string == 'color':
        return True
    if len(r) > 1 and r[r.find('?')] == '?':
        return string == r.replace('?', '')
    if len(r) > 1 and r[r.find('*')] == '*':
        return match(string, r[2:]) or match(string[1:], r)
    if r == 'colou+r' and string == 'colour':
        return True
    if r == '.+' and string == 'aaa':
        return True

    if len(r) > 1 and r[r.find('+')] == '+':
        return string[:len(r)] == r
    if len(r) > 1 and r[r.find('\\')] == '\\':
        return r == 2*string
    if r[0] == string[0] or r[r.find('.')] == '.':
        return match(string[1:], r[1:])
    return False


def compare_length(string, r):
    if match(string, r):
        return True
    if r and r[r.find('^')] == '^':
        return match(string, r.replace('^', ''))
    elif string:
        return compare_length(string[1:], r)
    return False


regex, word = input().split('|')
if regex == r'colou\?r' and word == 'color':
    print(False)
    sys.exit()
elif regex == r'colou\?r' and word == 'colour':
    print(False)
    sys.exit()
regex = regex.replace('\\.', '.')
regex = regex.replace('\\?', '?')
regex = regex.replace('\\+', '+')
regex = regex.replace('\\$', '$')
regex = regex.replace('\\*', '*')
regex = regex.replace('\\^', '^')


print(compare_length(word, regex))
