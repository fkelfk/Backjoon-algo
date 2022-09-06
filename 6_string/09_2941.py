# 2941
word = input()

croa_aphabet = {
    "č": "c=",
    "ć": "c-",
    "dž": "dz=",
    "đ": "d-",
    "lj": "lj",
    "nj": "nj",
    "š": "s=",
    "ž": "z=",
}

for i in croa_aphabet.values():
    if i in word:
        word = word.replace(i, "a")

