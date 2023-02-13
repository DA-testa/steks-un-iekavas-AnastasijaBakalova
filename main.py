# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            check = ")]}".index(next)
            match check:
              case 0:
                a='('
              case 1:
                a='['
              case 2:
                a = '{'
            if (len(opening_brackets_stack)>0) and (opening_brackets_stack[len(opening_brackets_stack)-1] == a):
               opening_brackets_stack.pop()
            else: return i+1
    if len(opening_brackets_stack)==0: return -1
    else : return len(text)


def main():
    text1 = input()
    if (text1[0] == "I"):
      text = input()
      mismatch = find_mismatch(text)
      if (mismatch==-1):
          print('Success')
      else: print(mismatch)


if __name__ == "__main__":
    main()
