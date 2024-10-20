#!/bin/bash

VIMRC="$HOME/.vimrc"
if [ ! $(grep -l syntax ~/.vimrc 2>/dev/null) ]
then
    echo "syntax on" >>$VIMRC
fi

if [ ! $(grep -l tabstop ~/.vimrc 2>/dev/null) ]
then
    echo "set tabstop=4" >>$VIMRC
fi

if [ ! $(grep -l shiftwidth ~/.vimrc 2>/dev/null) ]
then
    echo "set shiftwidth=4" >>$VIMRC
fi

if [ ! $(grep -l expandtab ~/.vimrc 2>/dev/null) ]
then
   echo "set expandtab" >>$VIMRC
fi
