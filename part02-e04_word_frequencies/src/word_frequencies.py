#!/usr/bin/env python3

def word_frequencies(filename):
    f = open(filename, "r+")
    res={}
    for line in f:
        splitted = line.split()
        stripped = [i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in splitted]
        words = line.strip("""!"#$%&'()*,-./:;?@[]_""").split()
        print(words)
        for w in stripped:
            if w in res.keys():
                res[w] += 1
            else: res[w] = 1
    print(res['Project'])
    return res

def main():
    word_frequencies("src/alice.txt")
    pass

if __name__ == "__main__":
    main()
