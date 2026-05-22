from sys import argv

script, username = argv

prompt = '>'

print(f"hi this {username} im {script} script.")
print ("do ypu like me?")
likes = input(prompt)

print(f"you have said '{likes}' about liking me")
