def get_num_words(book_location):
    words_number = 0
    with open(book_location) as content:
        book_content = content.read()
    words = book_content.split()
    for word in words:
        words_number += 1
    print("----------- Word Count ----------")
    print(f"Found {words_number} total words")    

def get_num_caracters(book_location):
    dicionario = {}
    NewDict = []
    i = 0
    with open(book_location) as content:
        book_content = content.read()
    book_content_under = book_content.lower()
    words = book_content_under.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter in dicionario:
                    dicionario[letter] += 1
                else:
                    dicionario[letter] = 1
    print("--------- Character Count -------")
    for char , count in sorted(dicionario.items(), key=lambda item:item[1],reverse=True):
       print(f"{char}: {count}")
    
    print("============= END ===============")
    

def orderDict(NewDict):
    return NewDict["num"]
