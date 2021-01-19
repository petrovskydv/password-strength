import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isalpha() and not letter.isdigit() for letter in password)


def doesnt_consist_of_symbols(password):
    return any(letter.isalpha() or letter.isdigit() for letter in password)


def on_ask_change(edit, new_edit_text):
    print(new_edit_text)
    score = 0
    cheks_list = [is_very_long, has_digit, has_letters, has_upper_letters, has_lower_letters, has_symbols]
    for chek in cheks_list:
        if chek(new_edit_text):
            score += 2
    print('Рейтинг этого пароля:', score)


if __name__ == '__main__':
    ask = urwid.Edit('Введите пароль: ')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
