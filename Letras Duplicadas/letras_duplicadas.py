def duplicate_count(text):
    return len([letter for letter in set(text.lower()) if text.lower().count(letter) > 1]) 


if __name__ == '__main__':
    duplicate = duplicate_count('aA111a22')
    print('Letters duplicated: ', duplicate)
