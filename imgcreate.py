import requests
prompt="Girl sitting on a bench in a park, surrounded by blooming flowers and trees, with a serene expression on her face."
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("y.png","wb") as f:
    f.write(img)
    