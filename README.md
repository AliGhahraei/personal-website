# AliGhahraei.github.io
Personal website.

This site is generated with the help of [Pelican](https://blog.getpelican.com/). Its source files
are in the *src* branch of this repository.

## Requirements
* Python 3

You should also have the site's theme in the correct location. These settings are near the bottom of
pelicanconf.py and look like this:

```python3
USER_THEME_PATH = expanduser(join('local, path', 'to', 'theme'))
THEME_NAME = 'site_theme'
THEME = join(USER_THEME_PATH, THEME_NAME)
```

So place the theme specified by THEME_NAME (*site_theme* in the example) in USER_THEME_PATH
(*/local/path/to/theme*)
