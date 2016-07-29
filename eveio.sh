#!/bin/sh

CURRENT=$(cd `dirname $0`; pwd)
PROJECT=`dirname $CURRENT`

LIBEIO_TAG="rel-4_19"
LIBEIO_SO="libeio.so.1.0.0"

LIBV_TAG="rel-4_22"
LIBEV_SO="libev.so.4.0.0"

cd /tmp
cvs -z3 -d :pserver:anonymous@cvs.schmorp.de/schmorpforge co -r $LIBEIO_TAG libeio
cd libeio
chmod +x autogen.sh
./autogen.sh
./configure && make
cp -rf .libs/$LIBEIO_SO $PROJECT/lib/$LIBEIO_SO

cd /tmp
cvs -z3 -d :pserver:anonymous@cvs.schmorp.de/schmorpforge co -r $LIBEV_TAG libev
cd libev
chmod +x autogen.sh
./autogen.sh
./configure && make
cp -rf .libs/$LIBEV_SO $PROJECT/lib/$LIBEV_SO

cd /tmp
rm -rf libeio
rm -rf libeio
