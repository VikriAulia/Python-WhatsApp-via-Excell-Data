<div align="center">
# Python-WhatsApp-via-Excell-Data
pywhatkit + Pandas 


[Installation](#Installation) •
[How to use](#How-to-use)
</div>

## Installation
```sh
pip install git+https://github.com/vikriaulia/Python-WhatsApp-via-Excell-Data.git
```

## How to use
You have a lot of parameters!
```sh
cscrape --url https://sendokame.netlify.app --tag "a" # <- You can select the attributes of BS4. 
```
Or
```sh
cscrape --url https://alansierra.xyz/blog/ --selector 'a > h2'
```
<br>

There are filters!
```sh
                                            |Python oneline code that outputs Node attributes
cscrape --url https://example.com --tag "p" --filter "node.attrs"
                                   |You can use Tags or Selector
```