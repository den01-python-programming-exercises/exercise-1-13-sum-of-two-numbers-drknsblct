def main():
    #write your code below this line
    first = int(input('Give the first number:'))
    second = int(input('Give the second number:'))

#     print(f'The sum of the numbers is {first + second}')
#     flake8 doesn't understand f-strings for some reason...

    print('The sum of the numbers is ' + str(first + second)')


if __name__ == '__main__':
    main()
