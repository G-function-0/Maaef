import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove the fixed height from the menu a tags
    content = content.replace(" h-[80px] md:h-[130px]", "")
    
    # 2. Add padding and block display to the static spans
    content = re.sub(
        r'(<span[^>]*class="[^"]*)(group-hover:-translate-y-full)(")',
        r'\1pb-2 md:pb-6 block \2\3',
        content
    )
    
    # 3. Add padding, block display, and full width to the absolute spans
    content = re.sub(
        r'(<span[^>]*class="[^"]*)(translate-y-full group-hover:translate-y-0)(")',
        r'\1w-full pb-2 md:pb-6 block \2\3',
        content
    )
    
    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
