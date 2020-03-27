from password_generator import generate_password
from sys import argv, exc_info
from getopt import gnu_getopt as getopt, GetoptError

LONG_OPTIONS = [
    'no-digits',
    'no-lower',
    'no-upper',
    'no-symbols'
]

def help():
    print('python . <length> [OPTIONS]')
    print()
    print('\t<length>\tNumber of characters in the password')
    print()
    print('\t--no-digits\tNo digits in the password')
    print('\t--no-symbols\tNo symbols in the password')
    print('\t--no-lower\tNo lowercase letters in the password')
    print('\t--no-upper\tNo uppercase letters in the password')
    print()
    print('\t-h\t\tHelp')
    print()

def main(argv):
    try:
        opts, args = getopt(argv, 'h', LONG_OPTIONS)
        length = 16
        if len(args) and args[0].isdigit():
            length = int(args[0])

        opt_list = []
        for opt, _ in opts:
            if opt == '-h':
                help()
                exit()
            else:
                opt_list.append(opt[2:])

        options = []
        for option in LONG_OPTIONS:
            if not option in opt_list:
                options.append(option[3:])

        if not len(options):
            raise GetoptError('Can\'t generate password with no char type')
    except GetoptError as err:
        print(err)
        help()
    except:
        print(exc_info())
        help()
    else:
        print(generate_password(length, options))


if __name__ == '__main__':
    main(argv[1:])
