import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Fix the Big text CTA container breakout.
    # The normal structure has:
    #                 </div> <!-- column -->
    #             </div> <!-- grid -->
    #             <!-- Big text CTA -->
    # We want to add a third </div> before <!-- Big text CTA --> to close max-w-[1400px].
    
    if '<!-- Big text CTA -->' in content:
        # First, ensure it's not already closed with 3 </div>s
        match_3 = re.search(r'</div>\s*</div>\s*</div>\s*<!-- Big text CTA -->', content)
        if not match_3:
            # Check if there are 2 </div>s
            match_2 = re.search(r'</div>\s*</div>\s*<!-- Big text CTA -->', content)
            if match_2:
                content = re.sub(
                    r'(</div>)(\s*)(<!-- Big text CTA -->)',
                    r'\1\n        </div>\2\3',
                    content
                )
    
    # 2. Fix the tapes to 200% width
    if '<!-- Police Tape 1 -->' in content:
        content = re.sub(
            r'absolute left-\[-10%\] right-\[-10%\] w-\[120%\]',
            r'absolute left-[-50%] right-[-50%] w-[200%]',
            content
        )
        # Also fix expertise/pinhole if they use -25%
        content = re.sub(
            r'absolute left-\[-25%\] right-\[-25%\] w-\[150%\]',
            r'absolute left-[-50%] right-[-50%] w-[200%]',
            content
        )

    # 3. Bottom bar wrapper
    if '<!-- Bottom bar -->' in content:
        # Check if already wrapped
        match = re.search(r'<div class="max-w-\[1400px\] mx-auto px-6 md:px-12 relative z-10">\s*<!-- Bottom bar -->', content)
        if not match:
            # We add the wrapper
            content = re.sub(
                r'(<!-- Bottom bar -->)',
                r'<div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">\n            \1',
                content
            )
            # And close it after Bottom bar. The Bottom bar is just a div block. 
            # It's safer to just replace the footer closing tag.
            # But wait, there is already logic I ran before:
            # content = re.sub(r'(</div>)(\s*<!-- Bottom bar -->)', r'\1\n\n        <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">\2', content)

    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
