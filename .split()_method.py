# the delimiter can be anything. If you just leave empty parenthesis it will wil default to spaces
# howevery you can put any character you want in between the '' quotation marks in the () parenthesis
words = 'You=a=bitch'
print(words.split('='))

words = 'You a bitch'
print(words.split())

words = 'You a bitch'
print(words.split(' '))
