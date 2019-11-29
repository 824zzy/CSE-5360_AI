#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 07/22/2013  
# Notes:       *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from copy import deepcopy


symbolsList = set()
#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print '\nINVALID\n'

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective,result)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol,result)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print '\nUnexpected end of input.\n'
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target,tempResult):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            if target is tempResult.symbol:
                symbolsList.add(target[0])
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# End of ported code
#-------------------------------------------------------------------------------

# Add all your functions here

def getConstants(model, knowledge_base):
    for expr in knowledge_base.subexpressions:
        if len(expr.connective) == 1 and len(expr.subexpressions) == 0:
            model[expr.symbol[0]] = True

            if expr.symbol[0] in symbolsList:
                symbolsList.remove(expr.symbol[0])
        elif expr.connective[0] == 'not' and len(expr.subexpressions[0].subexpressions) == 0:
            model[expr.subexpressions[0].symbol[0]] = False

            if expr.subexpressions[0].symbol[0] in symbolsList:
                symbolsList.remove(expr.subexpressions[0].symbol[0])
    return

def evalStatements(expression, model, valuesList):

    if expression.symbol[0] and expression.symbol[0] != '':
        return model[expression.symbol[0]]
    elif expression.connective[0]:
        for subexpression in expression.subexpressions:
            valuesList.append(evalStatements(subexpression, model, []))

        if len(valuesList) > 0:
            start = valuesList.pop()
        else:
            if expression.connective[0] == 'and':
                return True
            elif expression.connective[0] in ['or', 'xor']:
                return False
        if expression.connective[0] == 'not':
            return (not start)

        elif expression.connective[0] == 'and':
            if start and all(valuesList):
                start = True
            else:
                start = False

            return start

        elif expression.connective[0] == 'or':
            while(len(valuesList) > 0):
                end = valuesList.pop()

                if start or end:
                    start = True
                else:
                    start = False
            return start

        elif expression.connective[0] == 'xor':
            while(len(valuesList) > 0):
                if start != valuesList.pop():
                    return True
                else:
                    return False

        elif expression.connective[0] == 'if':
            while(len(valuesList) > 0):
                start = (not valuesList.pop()) or start
            return start

        elif expression.connective[0] == 'iff':
            if start == valuesList.pop():
                return True
            else:
                return False


def pl_true(expression, model):
    return evalStatements(expression, model, [])


def tt_check_all(knowledge_base, statements, symbols, model):
    
    truethValues = []
    symbolsLen = len(symbols)
    tt_counter = 0
    ttString = bin(tt_counter)[2:].zfill(symbolsLen)
    while ttString != ('1' * symbolsLen):

        for index, sym in enumerate(symbols):
            model[sym] = bool(int(ttString[index]))

        if pl_true(knowledge_base, model):
            truethValues.append(pl_true(statements, model))

        tt_counter = tt_counter + 1
        ttString = bin(tt_counter)[2:].zfill(symbolsLen)
    return truethValues

def bin(st):
    
    if st < 0: 
        return '-' + bin(-st)
    out = []
    if st == 0: 
        out.append('0')
    while st > 0:
        out.append('01'[st & 1])
        st >>= 1
        pass
    try: 
        return '0b' + ''.join(reversed(out))
    except NameError, ne2: 
        out.reverse()
    return '0b' + ''.join(out)

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
    
