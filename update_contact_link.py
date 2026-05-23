import os
files = ['index.html', 'about.html', 'contact.html', 'services.html', 'expertise.html', 'pinhole.html', 'Maaef Direction A.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace("onclick=\"window.location.href='/contact'\"", "onclick=\"window.location.href='/contact.html'\"")
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('Updated', filename)
