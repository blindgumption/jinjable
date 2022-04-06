"""
usual setuprepl module
"""

import webbrowser as wb 
from apija import config 
env = config.initEnv()
bh = env.get_template('basic.html')

def writeTmpHtml(th):
    with open('tmp.html', 'w') as f:
        f.write(th)

## end of file 