OUTPUT=/Users/grantwilkins/Jarvis/src/


all: barbot

barbot: barbot.proto
	python3 -m grpc_tools.protoc barbot.proto -I$(PWD) --python_out=$(OUTPUT) --pyi_out=$(OUTPUT) --grpc_python_out=$(OUTPUT)