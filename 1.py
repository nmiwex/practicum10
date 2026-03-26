def count_letters(sentence: str):
    """
    counts the number of vowels and consonants in a sentence in Russian
    :return: None
    """
    vowels = 'уеыаоэяиюё'
    consonants = 'бвгджзйклмнпрстфхцчшщ'
    v_count = 0
    c_count = 0

    for ch in sentence.lower():
        if ch in vowels:
            v_count += 1
        elif ch in consonants:
            c_count += 1

    print(f'Гласных: {v_count}, согласных: {c_count}')