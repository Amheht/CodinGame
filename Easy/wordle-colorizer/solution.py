# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/wordle-colorizer
import sys

def countsDict(text: str) -> dict:
    s = {}
    for char in text: 
        if char in s.keys():
            s[char] = s[char] + 1
        else:
            s[char] = 1
    return s

def solve(guess, answer):
    ans_dict = countsDict(answer)
    review = []
    s = ["?", "?", "?", "?", "?"]
    for c, char in enumerate(guess):
        if char == answer[c]:
            ans_dict[char] -= 1
            s[c] = "#"

        elif not char in answer:
            s[c] = "X"

        elif answer.count(char) == guess.count(char):
            ans_dict[char] -= 1
            s[c] = "O"
        
        else:
            review.append(c)
            
    for index in review:
        if ans_dict[guess[index]] > 0:
            s[index] = "O"
            ans_dict[guess[index]] -= 1
        else:
            s[index] = "X"
    return "".join(s)

answer = input()
n = int(input())

for i in range(n):
    attempt = input()
    solution = solve(attempt, answer)
    print(solution)
    print(file=sys.stderr, flush=True)
  
