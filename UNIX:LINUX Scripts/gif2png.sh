if [ $# -eq 0 ]
then
    echo "Usage: $0 files..." 1>&2
    exit 1
fi

if ! type giftopnm 2>/dev/null
then
    echo "$0: conversion tool giftopnm not found " 1>&2
    exit 1
fi

# missing "in ..." defaults to in "$@"
for f
do
    case "$f" in
    *.gif)
        # OK, do nothing
        ;;
    *)
        echo "gif2png: skipping $f, not GIF"
        continue
        ;;
    esac

    dir=`dirname "$f"`
    base=`basename "$f" .gif`
    result="$dir/$base.png"

    giftopnm "$f" | pnmtopng > $result && echo "wrote $result"
done
