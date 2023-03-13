OUTPUT=/Users/grantwilkins/Jarvis/src/grpc/


all: barbot

barbot: barbot.proto
	protoc ./barbot.proto -I./ --python_out=$(OUTPUT) --pyi_out=$(OUTPUT) --grpc_python_out=$(OUTPUT)