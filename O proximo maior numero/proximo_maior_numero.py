import itertools


def next_bigger(n):
    ''' Retorno o proximo maior numero'''
    num = str(n)
    listOfNums = set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])   
    listOfNums = sorted(list(listOfNums))
    try:
        return listOfNums[listOfNums.index(n)+1]
    except Exception:
        return -1

if __name__ == '__main_':
    print(next_bigger(513))