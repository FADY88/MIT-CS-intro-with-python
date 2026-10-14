# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext : ps4b.EncryptedMessage, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    dictionary = load_words(WORDLIST_FILENAME)
    highest_count = 0
    best_pad = None
    for i in range(len(pads)):
        text = ciphertext.decrypt_message(pads[i]).get_text().split(' ')
        word_count = 0
        for word in text:
            if is_word(dictionary, word):
                word_count += 1
        if word_count >= highest_count:
            highest_count = word_count
            best_pad = pads[i]
    return ps4b.PlaintextMessage(ciphertext.decrypt_message(best_pad).get_text(), best_pad)



def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    pads = get_story_pads()
    text = ps4b.EncryptedMessage(get_story_string())
    textMessage = decrypt_message_try_pads(text, pads)
    return textMessage.get_text()



if __name__ == '__main__':
    # Uncomment these lines to try running decode_story()
    story = decode_story()
    # print("Decoded story: ", story)
    text = ps4b.PlaintextMessage('In cryptography, Alice and Bob are fictional characters commonly used as placeholders in discussions about cryptographic protocols or systems, and in other science and engineering literature where there are several participants in a thought experiment. The Alice and Bob characters were invented by Ron Rivest, Adi Shamir, and Leonard Adleman in their 1978 paper "A Method for Obtaining Digital Signatures and Public-key Cryptosystems". Subsequently, they have become common archetypes in many scientific and engineering fields, such as quantum cryptography, game theory and physics.[2] As the use of Alice and Bob became more widespread, additional characters were added, sometimes each with a particular meaning. Source wikipedia: https://en.wikipedia.org/wiki/Alice_and_Bob', [91, 69, 59, 32, 86, 2, 59, 66, 7, 74, 53, 61, 50, 38, 78, 38, 91, 15, 90, 86, 14, 84, 25, 90, 56, 85, 51, 94, 68, 14, 49, 15, 42, 37, 89, 34, 7, 9, 69, 13, 27, 10, 58, 62, 
    26, 55, 62, 28, 28, 56, 63, 12, 56, 79, 49, 0, 17, 15, 52, 52, 85, 19, 9, 73, 25, 60, 69, 92, 17, 34, 78, 53, 43, 79, 35, 32, 34, 7, 46, 34, 60, 24, 33, 8, 28, 40, 18, 73, 73, 23, 84, 12, 79, 43, 65, 5, 75, 20, 6, 73, 52, 1, 77, 74, 66, 46, 27, 87, 4, 8, 
    4, 39, 20, 25, 9, 17, 56, 82, 32, 0, 21, 83, 20, 5, 82, 63, 35, 28, 67, 52, 57, 53, 24, 59, 45, 75, 66, 62, 62, 29, 42, 16, 9, 78, 76, 64, 28, 27, 16, 9, 38, 7, 22, 21, 76, 17, 2, 84, 60, 0, 38, 54, 27, 78, 9, 50, 59, 2, 89, 76, 83, 80, 81, 0, 34, 26, 8, 
    40, 80, 23, 62, 70, 63, 9, 67, 57, 72, 28, 49, 38, 2, 78, 4, 41, 64, 35, 10, 92, 90, 15, 70, 4, 71, 1, 19, 38, 17, 62, 86, 22, 21, 17, 31, 9, 63, 67, 7, 86, 57, 19, 4, 57, 36, 35, 26, 6, 0, 35, 58, 18, 18, 71, 73, 63, 9, 90, 23, 82, 67, 91, 53, 7, 89, 53,
    51, 38, 87, 63, 41, 43, 91, 58, 81, 71, 18, 83, 41, 61, 85, 93, 60, 22, 91, 45, 32, 21, 69, 25, 38, 61, 49, 12, 8, 20, 54, 88, 43, 8, 11, 11, 80, 58, 8, 33, 3, 38, 59, 1, 74, 74, 90, 2, 32, 32, 45, 66, 53, 43, 32, 73, 87, 26, 75, 90, 62, 9, 77, 28, 64, 16,
    88, 54, 42, 20, 10, 88, 25, 25, 93, 80, 72, 29, 15, 89, 85, 10, 58, 41, 55, 52, 61, 58, 65, 46, 1, 67, 81, 41, 20, 73, 72, 92, 43, 4, 85, 10, 88, 2, 85, 52, 64, 37, 63, 65, 50, 49, 63, 58, 2, 20, 66, 81, 1, 25, 44, 6, 90, 81, 61, 39, 71, 56, 74, 43,
    70, 49, 25, 31, 10, 54, 43, 16, 8, 94, 10, 72, 85, 67, 52, 58, 15, 64, 57, 25, 47, 12, 44, 42, 17, 82, 63, 8, 61, 53, 4, 10, 11, 5, 83, 20, 22, 31, 31, 13, 79, 9, 41, 17, 69, 42, 73, 54, 48, 19, 39, 83, 73, 80, 87, 49, 6, 89, 72, 89, 27, 9, 88, 87, 72, 92, 
    4, 36, 55, 30, 11, 42, 7, 85, 70, 7, 2, 58, 50, 27, 21, 32, 21, 92, 71, 85, 67, 84, 77, 50, 54, 79, 53, 46, 88, 41, 21, 91, 92, 80, 53, 26, 2, 8, 56, 48, 78, 91, 20, 61, 68, 41, 59, 88, 16, 69, 44, 87, 61, 35, 59, 79, 92, 4, 71, 87, 90, 79, 32, 67, 67, 1,
    31, 41, 87, 83, 32, 52, 17, 48, 7, 7, 22, 83, 85, 30, 33, 92, 26, 48, 50, 7, 82, 35, 33, 12, 51, 28, 0, 52, 62, 50, 91, 38, 30, 65, 49, 34, 87, 4, 15, 29, 55, 73, 79, 90, 49, 64, 16, 24, 91, 78, 23, 1, 73, 2, 23, 19, 94, 90, 18, 4, 77, 43, 40, 14, 72, 29,
    7, 88, 52, 26, 16, 61, 30, 35, 67, 21, 88, 33, 70, 55, 68, 13, 18, 26, 57, 65, 73, 4, 84, 2, 88, 93, 5, 16, 33, 56, 6, 61, 48, 20, 82, 87, 39, 65, 43, 80, 82, 15, 24, 46, 86, 18, 54, 42, 26, 84, 38, 2, 19, 39, 75, 72, 88, 74, 24, 75, 47, 92, 13, 3, 74, 
    78, 32, 78, 28, 26, 34, 78, 53, 24, 89, 69, 94, 32, 81, 75, 2, 80, 90, 40, 16, 53, 43, 47, 39, 56, 78, 12, 47, 71, 81, 23, 45, 33, 62, 50, 44, 77, 73, 13, 52, 70, 40, 80, 10, 35, 94, 91, 43, 0, 6, 23, 2, 2, 63, 51, 62, 54, 5, 51, 0, 59, 73, 10, 71, 62, 31,
    51, 59, 34, 32, 5, 37, 80, 2, 52, 57, 13, 50, 46, 61, 90, 25, 25, 84, 73, 4, 30, 13, 20, 5, 60, 46, 19, 89, 93, 65, 12, 10, 91, 38, 12, 35, 75, 38, 91, 43, 86, 85, 57, 19, 75, 43, 60, 49, 49, 50, 2, 75, 0, 45, 80, 32, 17, 62, 82, 55, 85, 27, 62, 68, 34, 66,
    43, 16, 93, 76, 47, 39, 21])
    print(text.get_ciphertext())