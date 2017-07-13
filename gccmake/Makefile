# LD_LIBRARY_PATH 环境变量来搜寻library

MY_LIBRARY_PATH = .
FILENAME = sum

.PHONY: run clean

run: test
	 export LD_LIBRARY_PATH=$(MY_LIBRARY_PATH):$LD_LIBRARY_PATH; \
	./test

clean:
	rm $(FILENAME).o lib$(FILENAME).so test

test: lib$(FILENAME).so
	gcc -L$(MY_LIBRARY_PATH) -Wall test.c -l$(FILENAME) -o test 

# -shared 表示要编译成 shared library
lib$(FILENAME).so: $(FILENAME).o
	gcc -shared $(FILENAME).o -o lib$(FILENAME).so

$(FILENAME).o: $(FILENAME).h
	gcc -c -Wall -fPIC $(FILENAME).c -o $(FILENAME).o

