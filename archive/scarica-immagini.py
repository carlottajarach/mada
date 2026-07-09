# -*- coding: utf-8 -*-
"""Scarica tutte le immagini del sito nella cartella images/.
Uso:  python scarica-immagini.py
"""
import os, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, 'images')
os.makedirs(IMG, exist_ok=True)
FILES = [
    ('logo.png', 'https://static.wixstatic.com/media/e51f31_32b0a12a79ff4bcc999b7c45cd715538~mv2.png'),
    ('logo-pink.png', 'https://static.wixstatic.com/media/e51f31_f0c89242f1f24240a3ca2477e796f2d6~mv2.png'),
    ('social-instagram.png', 'https://static.wixstatic.com/media/e1aa082f7c0747168d9cf43e77046142.png'),
    ('social-facebook.png', 'https://static.wixstatic.com/media/4057345bcf57474b96976284050c00df.png'),
    ('social-tiktok.png', 'https://static.wixstatic.com/media/11062b_69d309d6dbde492fae325fb0deca6556~mv2.png'),
    ('social-linkedin.png', 'https://static.wixstatic.com/media/aa0402eb9ba2430d9d0620b59556efca.png'),
    ('social-x.png', 'https://static.wixstatic.com/media/11062b_81cefb1bd2e2490d892a1cad5cc1cd8a~mv2.png'),
    ('social-youtube.png', 'https://static.wixstatic.com/media/45bce1d726f64f1999c49feae57f6298.png'),
    ('icon-linkedin-profile.png', 'https://static.wixstatic.com/media/48a2a42b19814efaa824450f23e8a253.png'),
    ('team-shirley.jpg', 'https://static.wixstatic.com/media/1cd938_b2b1a86877d84f8bb7c646d7e0a69a5c~mv2.jpg'),
    ('team-sharon.jpg', 'https://static.wixstatic.com/media/e51f31_6983c3e4fc024089bb30eecd551a2dca~mv2.jpg'),
    ('team-carlotta.jpg', 'https://static.wixstatic.com/media/e51f31_561a3bf91ca145bda8af2a3e0e7053a4~mv2.jpg'),
    ('partner-airc.png', 'https://static.wixstatic.com/media/e51f31_bc8aa51186f2420ab504a10c56a69b3f~mv2.png'),
    ('partner-cicap.png', 'https://static.wixstatic.com/media/e51f31_1900447e86444fa88ac4c739e6f6513b~mv2.png'),
    ('partner-science.png', 'https://static.wixstatic.com/media/e51f31_9b7a276f51694bf3b90ec2f65d6dae74~mv2.png'),
    ('partner-agora.png', 'https://static.wixstatic.com/media/e51f31_810f37620a744e0e9ac7b937017dfc1b~mv2.png'),
    ('evento-tuscia.png', 'https://static.wixstatic.com/media/e51f31_9eb032f71c0148ff9dd410de444356bb~mv2.png'),
    ('evento-sync.png', 'https://static.wixstatic.com/media/e51f31_1b0cc390e00b47a7a227c59ae0821f49~mv2.png'),
    ('evento-beatrice.png', 'https://static.wixstatic.com/media/e51f31_d28252ceb8f44f37b37fb516bfab5437~mv2.png'),
    ('post-trieste.jpg', 'https://static.wixstatic.com/media/e51f31_b3940206a1bf457dac0399df5ad69f01~mv2.jpg'),
    ('post-soldi.jpg', 'https://static.wixstatic.com/media/nsplsh_6c2f2348983e49d98296483799ef2551~mv2.jpg'),
    ('post-oppioidi.png', 'https://static.wixstatic.com/media/e51f31_f1bca035987e4516b15881b6af002d40~mv2.png'),
]
ok = 0
for fname, url in FILES:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(os.path.join(IMG, fname), 'wb') as f:
            f.write(data)
        print('  ok ', fname, '(%d KB)' % (len(data)//1024))
        ok += 1
    except Exception as e:
        print('  ERRORE su', fname, '->', e)
print('Scaricate %d/%d immagini in images/' % (ok, len(FILES)))
