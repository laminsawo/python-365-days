#!/usr/bin/env python

if __name__ == '__main__':

    def checkIfPrime(numberToCheck):

        if numberToCheck > 1:
            for num in range(2, numberToCheck):
                if numberToCheck % num == 0:
                    print(numberToCheck, ' is not a prime number')
                    break
                else:
                    print(numberToCheck, 'is a prime number')
                    break
        else:
            print(numberToCheck, 'is not a prime number')

    try:
        print('This program will check if a number is a Prime number or not')
        numberInput = int(input('Enter the number: '))
        checkIfPrime(numberInput)

    except ValueError:
        print('You did not enter a number. Please try again')
    except NameError:
        print('Had trouble in resolving a name')
    except TypeError:
        print('This operation is inappropriate')
    except Exception as e:
        print('Unknown error', e)
