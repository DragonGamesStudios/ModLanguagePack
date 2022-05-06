# Factorio Mod Language Pack
Factorio Mod Language Pack is a community maintained language pack for mods. It should be updated weekly, there might however be breaks in the updates, unless I manage to automate the process (which I doubt).

## If you are a user
There is no need for you to set up anything. Just download a release and (if you're not downloading directly from Factorio) place it in your mods directory. There are no dependencies and if the mod doesn't provide its own localization, it is guaranteed that you will see the translation in your game working properly. If you see any issues, report them, or correct them yourself and become a **contributor**, which I encourage you to do. You probably don't need to worry about long loading times. The translation loading should be pretty fast.

## If you are a modder
You are strongly encouraged to place your translations in this mod, thus becoming a contributor. Then all you need to do is to add a dependency on this mod.

## If you are a contributor
First of all, thank you for your contribution wether you've already submitted it or not.

There are a few guidelines as to how to contribute to the project.

### Creating a local branch
The mod is managed with git, so we can easily use its amazing features. So in order to contribute, you'll obviously need it: https://git-scm.com/

A good explanation of how to contribute to a project is here: https://opensource.com/article/19/7/create-pull-request-github.

### Writing translations
Unfortunately, Factorio doesn't allow for nested locale files. It does, however, allow for multiple files and all of them are loaded. So to utilize this and overcome the no-nested-directories problem, we can do the following: for every file in mod's original locale (most likely English), we create a file: `locale/<language>/<mod-name>-<file-name>.cfg`. If you want to update a translation or check if you have covered all the keys, you can simply run `python3 tools/compare.py <file1> <file2>` with the root directory as working directory.

### Correcting translations
If you want to correct any translation, simply edit the file. Note that when creating a pull request with translation correction, adding a brief explanation of the change would be welcome.

### Publishing your contribution
Once you're done, simply create a pull request. Remember to write in English and provide an explanation of what you've changed. Remember, that you'll contribute to the `experimental` branch, not to `master`, so create your new branch from `experimental`. I'll keep track of all contributors here: https://docs.google.com/spreadsheets/d/1PvdXGdRPD1WbMqIG2Jvn05gToqiFSLRwQ7D2rQZGCAE/edit?usp=sharing. If you don't want your name to appear in the contributors column, simply inform me about it in the pull request.

### The effects
The mod should get weekly updates, so don't expect your changes to be seen immediately. Thank you for your contribution in advance!