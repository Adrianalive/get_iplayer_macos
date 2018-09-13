#!/bin/bash
GIPDIR=/usr/local/get_iplayer
GIPCLI=$GIPDIR/bin/get_iplayer
GIPWPM=$GIPDIR/bin/get_iplayer.cgi
export PATH="$GIPDIR/bin${PATH:+:${PATH}}" 
export PERL5LIB="$GIPDIR/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}" 
exec $GIPWPM --getiplayer $GIPCLI --listen 127.0.0.1 --port 1935 "$@"
