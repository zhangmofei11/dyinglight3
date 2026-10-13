import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/c33188d7c9c5ac7c2d7b333c087eb9fe"></script>
<script data-cfasync="false" src="https://bauval.org/14/b54657db33398204db73c21f9f374ccf"></script>
<script>
  atOptions = {
    'key' : '7d052cde9fbc4a0d4df720e59566d979',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/7d052cde9fbc4a0d4df720e59566d979"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-c33188d7c9c5ac7c2d7b333c087eb9fe"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'combat.html', 'weapons.html', 'skills.html', 'collectibles.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '7d052cde9fbc4a0d4df720e59566d979' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-c33188d7c9c5ac7c2d7b333c087eb9fe' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')