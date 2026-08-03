transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

start_state = 'q0'
final_state = 'q2'

string = input("Enter String: ")

current = start_state
path = [current]

for ch in string:
    if (current, ch) in transitions:
        current = transitions[(current, ch)]
        path.append(current)
    else:
        print("Invalid Input")
        exit()

print("Transition Path:")
print(" -> ".join(path))

if current == final_state:
    print("Accepted")
else:
    print("Rejected")