#!/bin/bash

# ACTIVITY 1 ---------------

age=$1

# Start the nested conditional logic
if [ "$age" -lt 13 ]; then
  echo "Child"
elif [ "$age" -lt 20 ]; then
  echo "Teen"
elif [ "$age" -lt 65 ]; then
  echo "Adult"
else
  echo "Elderly"
fi


# ACTIVITY 2 ---------------





