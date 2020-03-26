# ----------------------------
# Modules: are external libraries that you can include and use in your project
# providing additional functionality
#
import re  # Regular expressions module

string = "I AM NOT YELLING, she said. Though we knew it to not be true"
print(string)

new = re.sub('[A-Z]', '', string)

print(new)

new = re.sub('[A-Z]', '', string)
