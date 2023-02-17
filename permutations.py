def permutations(head, tail=''):
    print('HEAD:', head)
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            print('i', i, 'head[:i]', head[:i], 'head[i+1:]', head[i+1:], 'head[i]:', head[i], 'tail+', tail+head[i])
            permutations(head[:i] + head[i+1:], tail + head[i])

permutations('ab')
print('NEXT')
permutations('abc')
