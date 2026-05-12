import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Let's use re.sub for a more robust match.
    # We want to replace:
    # </div>
    # 
    # <!-- Big text CTA -->
    #
    # With:
    # </div>
    # </div>
    # 
    # <!-- Big text CTA -->
    
    # We should ensure we don't duplicate it.
    if '<!-- Big text CTA -->' in content:
        # First, check if it's already done:
        # A simple check: if we see two `</div>` right before `<!-- Big text CTA -->` separated by just whitespace.
        match = re.search(r'</div>\s*</div>\s*<!-- Big text CTA -->', content)
        if not match:
            # Not done yet. Replace one </div> with two </div>s
            content = re.sub(
                r'(</div>)(\s*<!-- Big text CTA -->)',
                r'\1\n        </div>\2',
                content
            )

    if '<!-- Bottom bar -->' in content:
        # Check if already done:
        match = re.search(r'<div class="max-w-\[1400px\] mx-auto px-6 md:px-12 relative z-10">\s*<!-- Bottom bar -->', content)
        if not match:
            content = re.sub(
                r'(</div>)(\s*<!-- Bottom bar -->)',
                r'\1\n\n        <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">\2',
                content
            )

    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
