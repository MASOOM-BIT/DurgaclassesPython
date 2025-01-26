'''
> It simplifies the process of resource management by ensuring that resources are properly acquired and released, even in the presence of exceptions. Here’s an overview of its key features and usage:

>>> Purpose of the with Statement:

> Resource Management: The with statement eliminates the need for explicit try, except, and finally blocks that are typically required for resource management. It automatically handles opening and closing resources, such as files, making the code cleaner and less error-prone134.
> Context Management: It utilizes context managers, which are objects that define methods for setting up and tearing down resources (e.g., opening and closing files). This ensures that resources are released as soon as they are no longer needed
'''
'''
Syntax : 
with open('filename.txt', 'r') as file:
    # Perform operations using file

'''

with open('RESOURCES/file_with_stmt.txt', 'w') as file:
    file.write('Durga\n')
    file.write('Software\n')
    file.write('Solutions\n')
    print('Is file closed:',file.closed)
print('Is file closed:',file.closed)
