#!/usr/bin/env python
# coding: utf-8

# # Name : Ammar Sheikh

# # Roll # : IOT047691

# In[1]:


import pyautogui
import webbrowser
import time


# In[2]:


youtube_url = "https://www.youtube.com/watch?v=MhYvz-50y0Y&t=395s&ab_channel=PIAIC"
facebook_url = "https://www.facebook.com/piaic"


# In[3]:


pyautogui.position()


# In[4]:


webbrowser.open(youtube_url)
time.slHTTPS://WWW.YOUTUBE.COM/WATCH?V=mHyVZ-50Y0y&T=395S&AB_CHANNEL=piaic
    eep(5)
x, y = 402, 633
pyautogui.click(x, y)
pyautogui.typewrite(youtube_url)
pyautogui.press('enter')


# In[5]:


time.sleep(5)
webbrowser.open(facebook_url)
time.sleep(5)
x, y = 352, 400
pyautogui.click(x, y)
time.sleep(5)
for i in range(1):
    pyautogui.scroll(-5)  # negative value to scroll down
    time.sleep(0.5) 
pyautogui.click(303, 349)


# In[ ]:




