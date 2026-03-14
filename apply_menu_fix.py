import glob
import re

def apply_fixes(content):
    # 1. Increase translation distance to 120% and add leading-[1.1]
    # Replace group-hover:-translate-y-full with group-hover:-translate-y-[120%] and add leading-[1.1]
    content = re.sub(
        r'(class="[^"]*serif text-6xl md:text-9xl [^"]*)group-hover:-translate-y-full',
        r'\1leading-[1.1] group-hover:-translate-y-[120%]',
        content
    )
    
    # Replace translate-y-full with translate-y-[120%] and add leading-[1.1]
    content = re.sub(
        r'(class="[^"]*serif text-6xl md:text-9xl [^"]*)translate-y-full',
        r'\1leading-[1.1] translate-y-[120%]',
        content
    )
    
    # 2. Add py-2 to menu-link group
    content = content.replace(
        'class="menu-link group relative overflow-hidden inline-block hover-trigger cursor-pointer pointer-events-auto"',
        'class="menu-link group relative overflow-hidden inline-block hover-trigger cursor-pointer pointer-events-auto py-2"'
    )
    
    return content

for file_path in glob.glob('d:/Maef/Maaef/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = apply_fixes(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Applied fixes to {file_path}")
    else:
        print(f"No changes needed for {file_path}")
