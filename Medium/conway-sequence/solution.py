# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/ide/puzzle/conway-sequence

r = int(input())
l = int(input())

_seq = [r]
for line in range(l-1):
    new_seq = []
    while _seq != []:     
        i = next((i for i in range(len(_seq)) if _seq[i] != _seq[0]), len(_seq))
        new_seq.extend([i, _seq[0]])
        _seq = _seq[i:] 
    _seq = new_seq   
print(*_seq)
