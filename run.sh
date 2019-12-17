# !bin/sh

# Check if python exist in the machine
if which python > /dev/null 2>&1;
then
    # Execute script
    python3 session-cleaner.py
else
    # Python is not installed
    echo "Python is not installed."
fi
