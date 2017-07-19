# py-folder-generator
a python script to generate project folder from text

![Screenshoot](https://raw.githubusercontent.com/hanipcode/py-folder-generator/master/assets/generate.gif)

## Use without install
You can use the script without installing (installing actually just copying the script to the $HOME/bin folder)
```
$ git clone https://github.com/hanipcode/py-folder-generator.git
$ cd py-folder-generator
$ chmod +x generate-folder
$ ./generate-folder [YOUR_CONFIG_FILE]
```

## Installing
You can install it so you can use this script anywhere in your system

```
$ git clone https://github.com/hanipcode/py-folder-generator.git
$ cd py-folder-generator
$ chmod +x install.sh
```

## USAGE
### Config File Convention
1. The name of the file could be anything
2. you use happen to structure your config file
3. You nest the folder by adding more hypen
4. name without extension would be considered as folder
5. but it will support config file convention like `.eslint` or `.babelrc` (a `.` in the first name of the file)

### Running the script
`$ generate-folder [YOUR_CONFIG_FILE]`

## Example of Config File
```
-src
--.babelrc
--App.js
--components
---common
----Button.js
---footer
----Copyright.js
--Pages
---Login.js
---Generate
----index.js
---Timeline
----index.js
----footer.js
--reducers
---index.js
--constants.js
--index.js
-api
--index.js
--loginapi
---index.js
```
You can also use whitespace if you think it would be more readable like
```
- src
- - .babelrc
- - App.js
...rest of config file
```
