#get setence from user

original = input("Please write a sentence: ").lower().strip()

#split sentence into words

words = original.split()

#loop trough words and convert into pig latin

new_words =[]

for word in words:
    if word[0] in "aeiou":
        new_word = word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos+1
            else:
                break
        cons = word[vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest+cons+"ay"
        new_words.append(new_word)

#stick words back toghether into sentence

output = " ".join(new_words)

#output the final string

print(output)

