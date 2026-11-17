def count_vowels_and_consonants(text: str) -> dict:

    suz = {'unli' : 0 ,'undosh' :0}

    unlilar = 'aeoiuAEOIU'

    for harf in text:
        if harf.isalpha():
            if harf in unlilar:
                suz['unli'] += 1
            else:
                suz['undosh'] += 1

    return suz
text = input("suzni kiriting")
print(count_vowels_and_consonants(text))