import time
# Open the file in read mode

def Capital(text):
     #not error handling
     with open(text, 'r') as file:
        content = file.read().upper()
#execute
print("Starting processing text...")
start= time.perf_counter()
Capital("text_1.txt")
print("ALL CAPITAL NOW")
print(f"Total time taken: {time.perf_counter() - start}")