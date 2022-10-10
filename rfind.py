#Example 1: rfind() With No start and end Argument

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")

 # Substring 'let it': 22
 # Substring 'small ': -1
 # Highest index where 'be,' occurs: 18

# Example 2: rfind() With start and end Arguments

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))

# -1
# 25
# -1
# 18