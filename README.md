# CZ-File-Encoder
One time I made a movie file format that used ZIP to contain data, like images (.png) and sounds (.wav). When I showed my friend, they later said they made a compression algorithm similar to this. All they did was rename a .zip file to a .cz file. So I made an actual format, and submitted a pull request. He proceeded to get very angry at me, saying he wanted to do it himself, even though he had made no attempt to do so. He deleted his repo, but I am keeping my repo up, as I am kinda proud of this project. I have removed all of the crap he used, like project toml files, and now it is just the source and this readme. If you are interested in the format, then allow me to demonstate.
## the format
| Type | Size (in bytes) | Notes |
| ----- | ---------------- | ----- |
| Digit | 1 | ASCII Digit representing the length of the length of the filename |
| Digits | prev | Series of ASCII digits representing the length of the filename |
| String | prev | String containing the name of the file |
| Digit | 1 | ASCII Digit representing the length of the length of the filedata |
| Digits | prev | Series of ASCII Digits representing the length of the filedata |
| Raw | prev | GZipped binary data containing the data of the file |

This format can be appended as many times as you like to an existing CZ file. This format is not very practical for speed and is entirely meant to be as small as possible. There is no easy way to implement directories besides putting a `/` in the filename, and there is no file index, but it is extremely small. While you can replace the digits with `uint64_t`s and not need to use ASCII, the way it currently is makes it easier to implement in python. I am too lazy to make a C port, especially considering how much more difficult it would be in C, but maybe I will in C++ someday. Maybe.
