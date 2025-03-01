import re

def ab_match_star(s):
    return bool(re.fullmatch(r'a*b*', s))

def ab_match_2to3(s):
    return bool(re.fullmatch(r'a(bb|bbb)', s))

def find_lowercase_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

def find_upper_lower(s):
    return re.findall(r'\b[A-Z][a-z]+\b', s)

def a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

def replace_spaces_commas_dots(s):
    return re.sub(r'[ ,.]', ':', s)

def snake_to_camel_case(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))

def split_by_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

def insert_spaces_before_uppercase(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

def camel_to_snake_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

print(ab_match_star("abb"))
print(ab_match_2to3("abb"))
print(find_lowercase_underscore("hello_world test_case another_example"))
print(find_upper_lower("Hello World Test"))
print(a_any_b("axb"))
print(replace_spaces_commas_dots("Hello, world. How are you?"))
print(snake_to_camel_case("this_is_snake_case"))
print(split_by_uppercase("SplitAtUpperCase"))
print(insert_spaces_before_uppercase("InsertSpacesBetweenWords"))
print(camel_to_snake_case("CamelCaseToSnake"))
