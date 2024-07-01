calls = 0
def count_calls(calls):
    print(calls)

def string_info(string):
    global calls
    calls += 1
    new = (len(string), string.upper(), string.lower())
    return new

def is_contains(string, list_to_search):
    global calls
    calls += 1
    for item in list_to_search:
        list1 = []
        list1.append(item.lower())
    if string.lower() in list1:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
