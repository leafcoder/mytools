#!/bin/bash

COMMAND=$1
CASSANDRA_HOME=~/Desktop/test/cassandra/apache-cassandra-3.4
CASSANDRA_BIN=$CASSANDRA_HOME/bin
PID_FILE=cassandra.pid

for dirname in ['logs', 'data']; do
	if [ ! -d $CASSANDRA_HOME/dirname ]; then
		mkdir $CASSANDRA_HOME/dirname;
	fi
done

function stop() {
	if [ ! -f $PID_FILE ]; then
		echo 'Cassandra is not running.';
		return 0;
	fi
	kill `cat $PID_FILE`;
	rm $PID_FILE;
}

function start() {
	if [ -f $PID_FILE ]; then
		echo 'Cassandra is running.';
		return 0;
	fi
	$CASSANDRA_BIN/cassandra -p $PID_FILE;
}

case $1 in
	'stop' )
		stop;
		;;
	'restart' )
		stop;
		start;
		;;
	'status' )
		$CASSANDRA_BIN/nodetool status;
		;;
	'cqlsh' )
		if [ $# > 4 ]; then
			$CASSANDRA_BIN/$@;
		else
			$CASSANDRA_BIN/cqlsh;
		fi
		;;
	*)
		start;
		;;
esac
