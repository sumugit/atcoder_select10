S = input()

text = ["maerd", "remaerd", "esare", "resare"]

txt = ""
ans = 0
# 文字列を逆順に並び替え
for s in S[::-1]:
    txt += s
    if txt in text:
        ans += len(txt)
        txt = ""

if ans == len(S):
    print("YES")
else:
    print("NO")