def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    token = words[0]
    cnt = 1
    result = ''
    
    for i, j in zip(words, words[1:] + ['']):
        if i == j:
            cnt += 1
        else:
            if cnt == 1:
                result += i
            else:
                result += (str(cnt) + i)
            token = j
            cnt = 1
    
    return len(result)
           
    

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])


t = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"    
]

result = [7,9,8,14,17]

for i in t:
    print(solution(i))
