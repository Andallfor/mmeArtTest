import cv2
import random

# no title starts with 'the'
# answer with either key or value, both are accepted
key = {
    'rel': 'realism',
    'cub': 'cubism',
    'nor': 'northern renaissance',
    'itr': 'italian renaissance',
    'rom': 'romanticism',
    'bar': 'baroque',
    'imp': 'impressionism',
    'abs': 'abstract',
    'pre': 'pre renaissance'
}

csv = []
with open('data.csv', 'r') as f:
    csv = f.readlines()

data = dict()
for i, line in enumerate(csv):
    line = line.replace('\n', '')
    parsed = line.split(',')
    parsed = [i.strip() for i in parsed]
    data[i + 1] = parsed

paintings = [i + 1 for i in range(len(data))]
random.shuffle(paintings)

score = 0
missed = []
for i in range(len(paintings)):
    img = cv2.imshow("painting", cv2.imread(f'images/{paintings[i]}.jpg'))
    cv2.waitKey(5)
    
    answer = input("Painting info:")
    answer = answer.replace('\n', '')
    
    correct = data[paintings[i]]
    isEra = False
    isName = False
    isYear = False
    isTitle = False

    if str(correct[0]) in answer:
        isTitle = True
    if str(correct[1]) in answer or key[correct[1]] in answer:
        isEra = True
    if str(correct[2]) in answer:
        isName = True
    if str(correct[3]) in answer:
        isYear = True
    print()
    print(f'Correct Answers:\nTITLE = {correct[0]}\nERA = {correct[1]}\nARTIST = {correct[2]}\nYEAR = {correct[3]}')
    
    if isTitle + isEra + isName + isYear >= 2:
        score += 1
    else:
        missed.append(correct[0])
    
    if (not (isTitle and isEra and isName and isYear)):
        print(f'Your Results: {isTitle + isEra + isName + isYear}/4 correct.')
        incorrect = 'Incorrect:'
        if not isTitle:
            incorrect += ' title'
        if not isEra:
            incorrect += ' era'
        if not isName:
            incorrect += ' artist'
        if not isYear:
            incorrect += ' year'
        print(incorrect)
        
        input("Press enter to continue")
    else:
        print('All correct')

print()
print(f'{score}/{len(paintings)}')
print(f'Missed: {missed}')