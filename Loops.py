attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]

# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

output = []

for v in values:
    output.append({attributes[0]:v[0], attributes[1]: v[1], attributes[2]: v[2]})

output = [{attributes[0]:v[0], attributes[1]: v[1], attributes[2]: v[2]} for v in values]

print(output)