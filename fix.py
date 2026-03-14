with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    line_num = i + 1
    # Skip CSS 662-851
    if 662 <= line_num <= 851:
        continue
    # Skip JS 1637-1777
    if 1637 <= line_num <= 1777:
        continue
    new_lines.append(line)

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
