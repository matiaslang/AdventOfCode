import json
import re


def checkCharInWord(num, word, rule):
    if(num >= len(word)):
        return True
    if(word[num + 1] == rule):
        return True
    return False


def passwordFunction(ruleLetter, ruleNumber, word):
    num = re.findall("\d{1,2}", ruleNumber.group(0))
    firstNum = int(num[0])
    secondNum = int(num[1])
    occurences = word[0].count(ruleLetter.group(0))
    if(checkCharInWord(firstNum, str(word), ruleLetter.group(0)) and not checkCharInWord(secondNum, str(word), ruleLetter.group(0))):
        return True
    if(checkCharInWord(secondNum, str(word), ruleLetter.group(0)) and not checkCharInWord(firstNum, str(word), ruleLetter.group(0))):
        return True
    print(num)
    print("rule")
    print(ruleLetter.group(0))
    print("firstNum")
    print(firstNum)
    print("secondNum")
    print(secondNum)
    print("word:")
    print(word)
    print("\n\n")
    return False


with open('data.json', 'r') as data_file:
    json_data = data_file.read()

i = json.loads(json_data)
i = i["data"]

amount = 0

for var in i:
    rule = re.search("\d{1,2}[-]\d{1,2}[ ]\w", var)
    ruleLetter = re.search("[a-z]", rule.group(0))
    ruleNumber = re.search("\d{1,2}[-]\d{1,2}", rule.group(0))
    word = re.findall("\w{4,29}", var)
    if(passwordFunction(ruleLetter, ruleNumber, word)):
        amount += 1
print(amount)
