# The compiler:
CC= gcc

# Flags:
CFLAGS= -Wall -Wextra -std=c99 -lm -g
# C files:
SOURCES=  main.c random.c stat.c adj.c sync.c perc.c lists.c

# Name of output:
TARGET= net

$(TARGET):
	$(CC) $(SOURCES) $(CFLAGS) -o $(TARGET)

clean:
	rm -f $(TARGET)

#valgrind:
#	valgrind --leak-check=yes ./$(TARGET)
