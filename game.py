import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play (word):
 word_display = "_" * len(word)
 guessed = False
 guessed_letters = []
 guessed_words = []
 tries = 6
 print ('Hadi baslayalim. %d hakkin var.' %(tries))
 print(word_display)
 print("\n")

 while not guessed  and tries > 0:
    guess = input ('Tahminde bulunun : ').upper()
    
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print('%s harfini daha once denediniz' %(guess))
        elif guess not in word:
            tries -= 1
            print('%s harfi kelimede yok. %d hakkin kaldi.' %(guess,tries))
            guessed_letters.append(guess)  
        else:
            print('%s harfi kelimede var.' %(guess))
            guessed_letters.append(guess)
            word_as_array = list(word_display)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_array[index] = guess
            word_display = "".join(word_as_array)
            if"_" not in word_display:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():
        if guess == word:
            guessed = True
            word_display = word 
        elif guess in guessed_words:
            print('%s bu kelimeyi daha once denediniz.' %(guess))
        else:
            print('Dogru cevap degil.') 
            guessed_words.append(guess) 
            tries -= 1
            
    else:
        print('Gecersiz tahmin!')    
    print(word_display)
    print("\n")
    
 if guessed:
    print('Tebrikler, bildiniz.')
 else:
  print('Maalesef olmadi. Dogru cevap : %s.' %(word))
     
     
def main():
    word = get_word()
    play(word)
    while input("Tekrar oynamak ister misiniz ? (E/H)\n").upper() == "E":
       word = get_word()
       play(word)
main()