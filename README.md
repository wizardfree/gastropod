
# gastropod 🐌

gastropod is a web page slug generator in the style of what.three.words

---
**_The words are kinda strange looking, how are they generated?_**
Glad you asked the words are randomly selected from a word bank provided by the [english_words](https://github.com/dwyl/english-words) repository namely the ```words_dictionary.json``` file.

## Installation

Grab the latest version of the script from this repo and also download the latest ```words_dictionary.json``` file from the [english_words](https://github.com/dwyl/english-words) repository.

### Example:
```
$ git clone https://github.com/wizardfree/gastropod.git
$ cd ./gastropod
$ curl -o words_dict.json https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json
👍

```

## Usage

```
#make it executable
sudo chmod +x ./gastropod.py
#execute it
./gastropod.py
```
## Sample output
```
$ ./gastropod.py 
acuminating.biabo.latchman
$ ./gastropod.py 
suiting.sinfonietta.stentorophonic
$ ./gastropod.py 
louty.hemapophysis.overfamiliarly

```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)