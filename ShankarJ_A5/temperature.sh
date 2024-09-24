#!/bin/bash

temp=$1

if [ "$temp" -lt 55 ]; then
  echo "Freezing"
else
  if [ "$temp" -lt 67 ]; then
    echo "Cold"
  else
    if [ "$temp" -lt 85 ]; then
      echo "Nice"
    else
      echo "Hot"
    fi
  fi
fi
