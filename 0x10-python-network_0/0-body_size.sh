#!/usr/bin/env bash
#a script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

curl -sI "$!" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
