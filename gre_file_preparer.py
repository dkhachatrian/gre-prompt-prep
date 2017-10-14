
# coding: utf-8

# In[1]:

import re
import os


# In[2]:

# where we'll dump our prepared text files
prompt_dir = 'gre_essay_prompts'
os.makedirs(prompt_dir, exist_ok = True)


# In[3]:

no_prompt_text = "[There were not enough examples to furnish this text file with a sample prompt of this type.]"

iss_header = """=======================================================
Issue Topic:
"""

arg_header = """=======================================================
Argument Topic:
"""


# In[4]:

iss_fp = 'gre_iss_pool_html.txt'
arg_fp = 'gre_arg_pool_html.txt'

fps = [iss_fp, arg_fp]
prompt_ll = [] #will have issue prompts, then arg prompts

splitter = """<div class="divider-50"><hr></div>"""
m = re.compile(r'<p>(.*)</p>')


# In[5]:

prompt_ll = [] #will have issue prompts, then arg prompts
txt = ''
for fp in fps:
    with open(fp) as f:
        txt = ''.join(f.readlines())
        split_txt = txt.split(splitter)
        prompt_ll.append(['\n\n'.join(m.findall(t)) for t in split_txt[1:]]) #first entry does not contain prompts


# In[6]:

len2entry = {len(prompt_ll[i]):i for i in range(len(prompt_ll))}


# In[7]:

list_index = len2entry[min(len2entry.keys())]


# In[8]:

while len(prompt_ll[list_index]) < max(len2entry.keys()):
    prompt_ll[list_index].append(no_prompt_text)


# In[9]:

# len(str(max(len2entry.keys())))


# In[10]:

for i, (iss, arg) in enumerate(zip(*prompt_ll)):
    txt_fn = "GRE_Prompt_Sample_{0:03d}.txt".format(i+1) # '3' due to above output
    with open(os.path.join(prompt_dir,txt_fn), mode = 'w') as f:
        f.write("Attempt Date: ")
        f.write('\n\n')
        f.write(iss_header)
        f.write(iss)
        for _ in range(40): #ensure other prompt is out of view
            f.write('\n')
        f.write(arg_header)
        f.write(arg)
        f.write('\n\n\n')
    
# should now have all prompts in prompt_dir

