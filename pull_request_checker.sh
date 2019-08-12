#!/bin/bash

GH_URL="https://api.github.com/repos/GregHilston/Code-Foo/pulls"
FIVE_MIN_IN_SECONDS=300

while true; do 
  date
  resp=$(curl -H "Accept: application/json" -s "$GH_URL")
  count=$(echo "$resp" | jq "length")
  echo "${count} pull requests found..."
  echo
  if [ "$count" -ne "0" ]; then
    say "grehg, get to work! you have ${count} pull requests to merge!"
  fi
  sleep $FIVE_MIN_IN_SECONDS
done
