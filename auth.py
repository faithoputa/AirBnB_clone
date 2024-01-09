#!/usr/bin/python3
import subprocess

def generate_authors_file():
    # Run git log command to get commit history
    git_log_command = "git log --format='%aN <%aE>' | sort -u"
    result = subprocess.run(git_log_command, shell=True, stdout=subprocess.PIPE, text=True)
    # Extract authors from the result
    authors = result.stdout.split('\n')
    # Remove empty lines
    authors = list(filter(None, authors))
    # Write authors to the AUTHORS file
    with open('AUTHORS', 'w') as authors_file:
        authors_file.write('\n'.join(authors))
        print('AUTHORS file generated successfully.'
