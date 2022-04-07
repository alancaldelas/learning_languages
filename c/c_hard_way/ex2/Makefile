CFLAGS=-Wall -g
SRC = $(wildcard *.c)
BIN = $(SRC:%.c=%)

all:
	cc ${CFLAGS} ${SRC} -o ${BIN}
clean:
	rm -f ${BIN}
