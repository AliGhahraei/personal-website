#!/bin/bash
original_dir=$(pwd)

if [ -d "$PELICAN_THEMES_PATH" ]; then
   cd $PELICAN_THEMES_PATH
   git pull
   cd $original_dir
else
   git clone https://github.com/getpelican/pelican-themes $PELICAN_THEMES_PATH
fi

if [ -d "$PELICAN_PLUGINS_PATH" ]; then
   cd $PELICAN_PLUGINS_PATH
   git pull
   cd $original_dir
else
   git clone https://github.com/getpelican/pelican-plugins $PELICAN_PLUGINS_PATH
fi
