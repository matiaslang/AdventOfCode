import json
import re


def passwordFunction(ruleLetter, ruleNumber, word):
    num = re.findall("\d{1,2}", ruleNumber.group(0))
    firstNum = num[0]
    secondNum = num[1]
    occurences = word[0].count(ruleLetter.group(0))
    if(int(occurences) >= int(firstNum) and int(occurences) <= int(secondNum)):
        return True
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
