<table><tr><td style="border: 1px solid; padding: 10px 12px;"><b>This repository contains a fork of the AutoKey utility which has been modified to support the GNOME/Wayland environment in addition to the X11 environment currently supported by <a href="https://github.com/autokey/autokey">the "official" version</b></a>.</td></tr></table>

# AutoKey

[![](https://img.shields.io/badge/IRC-%23autokey%20on%20Libera.Chat-blue.svg)](https://web.libera.chat/#autokey)
[![](https://badges.gitter.im/autokey/autokey.svg)](https://gitter.im/autokey/autokey "Join the chat at https://gitter.im/autokey/autokey")
[![](http://img.shields.io/badge/stackoverflow-autokey-blue.svg)](https://stackoverflow.com/questions/tagged/autokey "Ask and answer questions on StackOverflow")
[![](https://www.codetriage.com/autokey/autokey/badges/users.svg)](https://www.codetriage.com/autokey/autokey)

## About
[AutoKey](https://github.com/autokey/autokey), a desktop automation utility for Linux <s>and X11</s>, formerly hosted on [Google](https://code.google.com/archive/p/autokey/), has been updated to run on Python 3.

<s><b>Important</b>: This is an X11 application and, as such, will not function correctly when Wayland is in use instead of Xorg.</s>

## Installation
**Important**: Please remove previous installations of AutoKey fully before installing!

For detailed installation instructions, please visit the [Installing](https://github.com/autokey/autokey/wiki/Installing) page in our wiki.


## Documentation
AutoKey documentation is available [here](https://autokey.github.io/index.html) and, for versions prior to 0.96.0, [here](https://autokey.github.io/autokey/index.html). Example code and explanations for how AutoKey works can be found in our [wiki](https://github.com/autokey/autokey/wiki) and, in particular, on the [Features](https://github.com/autokey/autokey/wiki/Features) and [Example Scripts](https://github.com/autokey/autokey/wiki/Example-Scripts) pages. Additional information can be found by searching [Stack Overflow](https://stackoverflow.com/questions/tagged/autokey) and [GitHub](https://github.com/search?l=Python&q=autokey&ref=cmdform&type=Repositories).


## Support
Please do not request support on the issue tracker. Instead, head over to the autokey-users [Google Groups](https://groups.google.com/forum/#!forum/autokey-users) forum, [Gitter](https://gitter.im/autokey/autokey) web-based chat, on [IRC](https://web.libera.chat/#autokey) (#autokey on [Libera.Chat](https://libera.chat/guides/)), or [Stack Overflow](https://stackoverflow.com/questions/tagged/autokey).

We'd appreciate it if you take a look at our [Troubleshooting](https://github.com/autokey/autokey/wiki/Troubleshooting) wiki page before posting. You'll be more likely to get a good answer quickly by providing as much information as you can.

## Bug reports
Bug reports are welcome. Please use the [GitHub Issue Tracker](https://github.com/autokey/autokey/issues) to report bugs. When reporting a suspected bug, please make sure to include as much information as possible to expedite troubleshooting and resolution.

Here are some possible examples of the types of information you might need to provide:

* Details on how to reproduce the issue you are experiencing are always helpful.
* An [AutoKey error message](https://github.com/autokey/autokey/wiki/Troubleshooting#autokey-error-message) is helpful when something is wrong with your AutoKey script.
* An [AutoKey traceback](https://github.com/autokey/autokey/wiki/Troubleshooting#autokey-traceback) is helpful when AutoKey runs without crashing, a trigger was used, and the expected event either didn't occur or something other than the expected result occurred.
* A [Python traceback](https://github.com/autokey/autokey/wiki/Troubleshooting#python-traceback) is helpful when something is wrong with your AutoKey script, causing an exception to be shown in your AutoKey error message.

If you're not sure your issue is a bug or you'd like help with reporting it, you can post about it first on one of the [platforms used by our community](https://github.com/autokey/autokey/wiki/Community) and we'll assist you.

## Contributing or modifying the source
Pull requests are welcome from anyone who would like to modify or contribute to the source code. Useful tips for working with and testing the code can be found in the [CONTRIBUTORS.rst](https://github.com/autokey/autokey/blob/master/CONTRIBUTORS.rst) file. AutoKey also participates in [CodeTriage](https://www.codetriage.com/autokey/autokey), where members can sign up to receive a periodic email with a link to an open AutoKey issue that needs help./CONTRIBUTORS.rst

## Changelog
Our [changelog](https://github.com/autokey/autokey/blob/master/CHANGELOG.rst) is the best source of information for what's new and fixed in each release.

## License
AutoKey uses the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html). See the [LICENSE](https://github.com/autokey/autokey/blob/master/LICENSE) file for a plain text copy of the license.
