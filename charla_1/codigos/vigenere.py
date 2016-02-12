#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Fran Rúa
# Implementación en python do algoritmo de Vigenere
# Máis info en:
# https://es.wikipedia.org/wiki/Cifrado_de_Vigenère


from sys import argv
from getopt import getopt, GetoptError
from string import ascii_lowercase
from itertools import cycle


# definimos o alfabeto como variable global
ALPH = list(ascii_lowercase)


def usage():
    print 'Programa de cifrado mediante algoritmo de Vigenere\n. Uso:'
    print '-h, --help: mostra esta axuda'
    print '-i, --input: especifica un ficheiro de texto de entrada,'\
        'na ruta actual'
    print '-o, --output: especifica un ficheiro de saida'
    print '-d: desencripta un texto de entrada'
    print '-e: encripta un ficheiro de entrada'
    print '-k: establece unha clave para encriptar/desencriptar'
    exit(2)


def len_error(num):
    print 'Error, a lonxitude da clave debe ser como mínimo 3'
    exit(2)


def parse_options(argv):
    options = {'input_file': '', 'output_file': 'cyphertext.txt'}
    try:
        opts, args = getopt(argv, 'dehi:o:k:', ['input', 'output',
                                                'help', 'key'])
    except GetoptError:
        print('Invalid Argument\nWrite --help for usage information')
        usage()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-i", "--input"):
            options['input_file'] = arg
        elif opt in ("-o", "--output"):
            options['output_file'] = arg
        elif opt in ('-k', '--key'):
            if(len(arg) < 3):
                len_error(len(arg))
            else:
                options['key'] = arg
        elif opt in ('-e', '-d'):
            options['operation'] = opt
    return options


def invalid_argument(arg):
    print 'Opción inválida: ' + arg
    usage()


def read_file(path):
    try:
        file = open(path, 'r')
    except IOError as e:
        print 'Error ({0}), {1}:{2}.'.format(e.errno, path, e.strerror)
        exit(1)
    text = file.read()
    file.close
    return text


def write_file(text, path):
    try:
        file = open(path, 'w+')
    except IOError as e:
        print 'Error ({0}), {1}:{2}.'.format(e.errno, path, e.strerror)
        exit(1)
    file.write(text)
    file.close


def encrypt_text(options):
    cleartext = read_file(options['input_file'])
    cleartext = cleartext.lower()
    cyphertext = ''
    key = []
    for k in options['key']:
        key.append(ALPH.index(k))
    pool = cycle(key)
    for e in cleartext:
        if e == ' ':
            cyphertext += ' '
        elif e == '\n':
            continue
        else:
            cyphertext += ALPH[(ALPH.index(e) + next(pool)) % len(ALPH)]
    write_file(cyphertext, options['output_file'])


def decrypt_text(options):
    cyphertext = read_file(options['input_file'])
    cyphertext = cyphertext.lower()
    cleartext = ''
    key = []
    for k in options['key']:
        key.append(ALPH.index(k))
    pool = cycle(key)
    for e in cyphertext:
        if e == ' ':
            cleartext += ' '
        elif e == '\n':
            continue
        else:
            cleartext += ALPH[(ALPH.index(e) - next(pool)) % len(ALPH)]
    write_file(cleartext, options['output_file'])


def main(argv):
    options = parse_options(argv)
    if(len(argv) < 6):
        print 'Numero de parametros insuficiente'
        usage()
    if options['operation'] == '-e':
        encrypt_text(options)
    elif options['operation'] == '-d':
        decrypt_text(options)
    else:
        invalid_argument(options['operation'])
    exit(0)


if __name__ == '__main__':
    main(argv[1:])              # O primeiro elemento da lista e o nome do
    # propio programa, así que ignoramolo
