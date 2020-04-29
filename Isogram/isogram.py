
'''Is isogram if the word has not duplicate letter'''
def is_isogram(string):
    return len(string) == len(set(string.lower()))

if __name__ == '__main__':
    if is_isogram('abcde'):
        print('Is a Isogram')
    else:
        print('Is not a Isogram')
