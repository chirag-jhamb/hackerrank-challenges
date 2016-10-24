#Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
def ransom_note(magazine, ransom,m,n):
    for i in ransom:
        if i in magazine:
            magazine.remove(i)
            a=True
        else:
            a= False
            break
    return a


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom, m, n)
if(answer):
    print "Yes"
else:
    print "No"
