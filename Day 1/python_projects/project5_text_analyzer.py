#NOTE Text Analyzer

#Welcome Text

print('\n' + '=' * 60)
print('TEXT ANALYZER')
print('=' * 60)
print('Enter a Sentence or Para below!!')

text = input('Text Here: ').strip()

char_count_with_spaces = len(text)
char_count_without_spaces = len(text.replace(' ',''))
char_count_histogram = {}
for char in text:
    char_count_histogram[char] = char_count_histogram.get(char,0) +1 
palindrome_words = []
word_frequency = {}
unique_words = []
words = text.split()
words_count = len(words)
for word in words:
    clean = ''.join(char.lower() for char in word if char.isalnum())
    if not clean: continue
    word_frequency[clean] = word_frequency.get(clean, 0) + 1
    if (len(clean)>1 and clean== clean[::-1]):
        palindrome_words.append(clean)
for word, count in word_frequency.items():
    if count == 1:
        unique_words.append(word) 
    
sentence_count = text.count('.') + text.count('!') + text.count('?')
if sentence_count == 0 and len(text)>0:
    sentence_count = 1
reversed_text = text[::-1]
reversed_words = ' '.join(words[::-1])
uppercase_count = sum(1 for char in text if char.isupper())
lowercase_count = sum(1 for char in text if char.islower())
digit_count = sum(1 for char in text if char.isdigit())
special_count = char_count_without_spaces - uppercase_count - lowercase_count - digit_count

if words:
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
else:
    longest_word = 'N/A'
    shortest_word = 'N/A'
if words_count > 0:
    total_words_chars = sum(len(word) for word in words)
    average_words_len = total_words_chars / words_count
else: average_words_len = 0


# Display

print("\n" + '=' * 50)
print("Text Analysis Results")
print('=' * 50)

print('\nLENGTH STATS')
print('='*50)
print(f'Characters Count with Spaces: {char_count_with_spaces :>6}')
print(f'Character Count without Spaces: {char_count_without_spaces :>6}')
print(f'Words: {words_count :>6}')
print(f'Sentences: {sentence_count:>6}')

print('\nCharacter Breakdown')
print('='*50)
print(f'UpperCase Characters: {uppercase_count:>6}')
print(f'LowerCase Characters: {lowercase_count:>6}')
print(f'Digits: {digit_count:>6}')
print(f'Special Characters: {special_count:>6}')
for char, count in sorted(char_count_histogram.items()):
    if char == ' ': label='[SPACE]'
    elif char == '\n': label= '[NEW LINE]'
    else: label = char
    print(f'{label}: {count}')
    
print('\nWord Statistics')
print('='*50)
print(f'Longest Word: {longest_word} {len(longest_word)} characters')
print(f'Shortest Word: {shortest_word} {len(shortest_word)} characters')
print(f'Average Words Length: {average_words_len:.1f} characters')
print(f'Unique Words: {unique_words}')
print(f'Palindrome Words: {palindrome_words}')
print('\nReversed')
print('='*50)
print(f'Reveresed Text: {reversed_text}')
print(f'Reveresed Words: {reversed_words}')

# Exporting content to a seprate file : analysis.txt

with open('analysis.txt', 'w', encoding="utf-8") as file:
    file.write('\n' + '=' * 50)
    file.write('\nTEXT ANALYSIS REPORT')
    file.write('\n' + '=' * 50 + '\n\n')
    file.write('\n' + '=' * 50)
    file.write('\nLength Stats')
    file.write('\n' + '=' * 50 + '\n\n')
    file.write(f'\nCharacters Count with Spaces: {char_count_with_spaces :>6}')
    file.write(f'\nCharacter Count without Spaces: {char_count_without_spaces :>6}')
    file.write(f'\nWords: {words_count :>6}')
    file.write(f'\nSentences: {sentence_count:>6}')
    file.write('\n' + '=' * 50)
    file.write('\nCharacter Breakdown')
    file.write('\n' + '='*50 + '\n\n')
    file.write(f'\nUpperCase Characters: {uppercase_count:>6}')
    file.write(f'\nLowerCase Characters: {lowercase_count:>6}')
    file.write(f'\nDigits: {digit_count:>6}')
    file.write(f'\nSpecial Characters: {special_count:>6}')
    for char, count in sorted(char_count_histogram.items()):
        if char == ' ': label='[SPACE]'
        elif char == '\n': label= '[NEW LINE]'
        else: label = char
        file.write(f'\n{label}: {count}')
    file.write('\n' + '=' * 50)
    file.write('\nWord Statistics')
    file.write('\n' + '='*50 + '\n\n')
    file.write(f'\nLongest Word: {longest_word} {len(longest_word)} characters')
    file.write(f'\nShortest Word: {shortest_word} {len(shortest_word)} characters')
    file.write(f'\nAverage Words Length: {average_words_len:.1f} characters')
    file.write(f'\nUnique Words: {unique_words}')
    file.write(f'\nPalindrome Words: {palindrome_words}')
    file.write('\n' + '=' * 50)
    file.write('\nReversed')
    file.write('\n' + '='*50 + '\n\n')
    file.write(f'\nReveresed Text: {reversed_text}')
    file.write(f'\nReveresed Words: {reversed_words}')
print('\nAnalysis succesfully exported to "analysis.txt"')