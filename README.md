# Call ordinal inscription with Python Code

## Disclaimer

For now it's extracting `gen-brc-721` protocol data. This protocol uses `deploy inscription` like  [GBRC721 BitPunks | gen-brc-721 collection](https://ordinals.link/content/c3915284759eaba761f6e5acf64b50e1089fe62448b595f61a40407d71bfb85ei0).

The `data.py` code takes a `deploy inscription` parameter to generate folders and extract each trait in png format.

This code will evolve and it's only the first version.

## Init

Initially we need to create a virtual python environment with : `pipenv shell`.

After run `pipenv install --ignore-pipfile` to install every dependencies.

If it doesn't work try : `pipenv install --dev-dependencies`.

## Run

`python3 data.py 1a1427e31c91566fe7fb47d7f5c1b2130bea31219a08e1de794d45512319ee61i0`


Where the output is : 
```
Trait types :  ['background', 'window', 'table', 'ornaments', 'flowerpot', 'rose']
This is the collection blooming-flower with : 

Elements per trait :  {'background': 8, 'window': 12, 'table': 4, 'ornaments': 12, 'flowerpot': 8, 'rose': 12}
total element :  56
total arrangements :  442,368
```

With a `gen-brc-721` indexer we can get every images defined from year to day.


## Some inscriptions

- [Deploy gbrc721bitpunk](https://ordinals.link/content/c3915284759eaba761f6e5acf64b50e1089fe62448b595f61a40407d71bfb85ei0)
- [Mint gbrc721bitpunk element](https://ordinals.link/content/3daa69f249fdcbae751183df0367d94530b259fb15666859cf60e7caf902ace4i0)

- [Deploy blooming-flower](https://ordinals.link/content/1a1427e31c91566fe7fb47d7f5c1b2130bea31219a08e1de794d45512319ee61i0)

- [Deploy testdoge element](https://ordinals.com/content/fc0a648126364b17e4940964d81d170fb8da3047911690d309880c03855f0c7di0) : This deploy contains a mistake, there left a right close curledbrace at the end of inscription.
To get elements, I added manually in `extract_all_images` after `reponse_table`, `response_table.text = response_table.text + '}'` and this worked.
- [Mint testdoge element](https://ordinals.link/content/81ddb9ee2d836068ebf371a511b822f8799527dedd198155a11844d84f3f502fi0)

- [Deploy phantom-test-4](https://ordinals.com/content/70880ccedc33d746af608c14b1b4db3c4926589b0236b12f8b1b4540e9e3c6f1i0) : This deploy is very different than the other. My actual code can't treat this deployment.
We see a new element `wl` what I suppose to be 'WhiteList' but I'm not sure.
In place of `traits` we have `attributes`. Which is interesting with attributes here it's each one are defined from other inscriptions.
There also is a `collection` vector in place of defined each element separately : `slug`, `name`,... . 
- [Compile phantom-test-4](https://ordinals.link/content/d82cbd9b59aa70c3f311302816536661d1c9923753e18ae92e0e70256f23d031i0) : I don't know how to use these type of inscription.
- [Mint a phantom-test-4 element](https://ordinals.link/content/9550284a8d5244084581d62ce4642868622d6c4b39217b1d67a3e10484aac8fei0) : same I don't know how to interact with this collection.

- [wl operation in gen-brc-721 protocol](https://ordinals.link/content/f2c26b91c3e0a3052a0a1f1c959ca56fb0af083bc6973ba3e8383477a0941e88i0)

- [Research gen-brc-721 in Unisat explorer](https://unisat.io/search?q=c3915284759eaba761f6e5acf64b50e1089fe62448b595f61a40407d71bfb85ei0&type=text&p=1)



