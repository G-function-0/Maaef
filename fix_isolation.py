import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    content = content.replace('id="kinetic-menu"\n            class="fixed', 'id="kinetic-menu"\n            style="isolation: isolate; will-change: transform;"\n            class="fixed')
    content = content.replace('id="kinetic-menu"\n        class="fixed', 'id="kinetic-menu"\n        style="isolation: isolate; will-change: transform;"\n        class="fixed')
    content = content.replace('id="kinetic-menu" class="hidden', 'id="kinetic-menu" style="isolation: isolate; will-change: transform;" class="hidden')
    
    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed isolation on {file}")
