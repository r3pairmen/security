import os

with open('urls.txt', 'r') as urls_file, open('results.txt', 'w') as results_file:
    for url in urls_file:
        url = url.strip()
        cmd = f"python script.py -u '{url}' --host asdf.com --workers 150"
        cmd = cmd.replace('url', url)
        print(f'Running command: {cmd}')
        output = os.popen(cmd).read()
        results_file.write(f'Results for {url}:\n{output}\n')
