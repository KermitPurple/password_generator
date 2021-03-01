from random import choice

def generate_pass(length: int = 10, special_chars: bool = True) -> str:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    if special_chars:
        chars += '!@#$%^&*()<>?,./:;"\'\\|[]{}`~-_+= '
    return ''.join([choice(chars) for _ in range(length)])

if __name__ == '__main__':
    print(generate_pass(20))
