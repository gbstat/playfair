import sys
import numpy as np

tab = np.array(list("""PLAYFIREXMBCDGHKNOQSTUVWZ""")).reshape((5,5))

def get_coord(letter, tab):
    """Get table coordinates that match input letter
    """
    return np.where(letter== tab)

def update_index(i):
    """Increment row/column and wrap around"""
    return (i + 1)%5

def same_row(left, right):
    """Update bigrams in same row"""
    return ((left[0], update_index(left[1])), (right[0], update_index(right[1])))

def same_col(top, bottom):
    """Update bigrams in same column"""
    return ((update_index(top[0]), top[1]), (update_index(bottom[0]), bottom[1]))

def rectangle(first, second):
    """Update bigrams forming a rectangle"""
    return ((first[0],second[1]), (second[0],first[1]))

def encrypt_bigram(bigram, tab):
    """Determine if the bigram letters are in the same
    row, column, or rectangle.
    """
    c1 = get_coord(bigram[0], tab)
    c2 = get_coord(bigram[1], tab)
    if c1[0] == c2[0]:
        (c1n, c2n) = same_row(c1, c2)
        return ''.join([tab[c1n].item(), tab[c2n].item()])
    elif c1[1] == c2[1]:
        (c1n, c2n) = same_col(c1, c2)
        return ''.join([tab[c1n].item(), tab[c2n].item()])
    else:
        (c1n, c2n) = rectangle(c1, c2)
        return ''.join([tab[c1n].item(), tab[c2n].item()])


def pad_password(password):
    """Add X between duplicate letters and at end of strings
    of odd numbered length.
    """
    password = password.strip()
    password_new = password[0]
    for i in range(1, len(password)):
        if (password[i] == password[i - 1]):
            password_new += 'X'
        password_new += password[i]
    if (len(password_new)%2)==1:
        password_new += 'X'
    return password_new


def encrypt_password(password, tab):
    """Playfair cypher"""
    password = password.upper()
    padded_password = pad_password(password) + " "
    epassword = ''
    for i in range(0, len(padded_password) - 1,2):
        epassword += encrypt_bigram(padded_password[i:(i + 2)], tab)
    return epassword


if __name__ == "__main__":
    print(encrypt_password(sys.argv[1],tab))
