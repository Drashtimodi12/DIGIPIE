"""
file Parameter:-    file tells where the printed output should go.
    Normally, Python prints on the screen (console).
    But using file=, you can print inside a file (like .txt).

Why use it?     To save logs
    To save output inside a file
    For report generation
"""

f = open("File.txt", "w")
print("Hello Drashti!", file=f)
f.close()