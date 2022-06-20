import emoji
from time import sleep
i = 10
f = 0
p = 1
for c in range(i, f-1, -p):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:'*10))
