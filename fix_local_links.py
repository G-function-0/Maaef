import os
import re

def fix_links(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace /about with /about.html, etc.
            # We use word boundaries or quotes to avoid accidental replacements
            new_content = re.sub(r'href="/about"', 'href="/about.html"', content)
            new_content = re.sub(r'href="/services"', 'href="/services.html"', new_content)
            new_content = re.sub(r'href="/contact"', 'href="/contact.html"', new_content)
            new_content = re.sub(r'href="/expertise"', 'href="/expertise.html"', new_content)
            
            if new_content != content:
                print(f"Updating links in {filename}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    fix_links(".")
