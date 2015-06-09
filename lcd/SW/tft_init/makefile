all: tft_init

tft_init: tft_init.o tft.o ST7789.o bmp.o
	gcc tft_init.o tft.o ST7789.o bmp.o -lbcm2835 -lrt -o tft_init

tft.o: tft.c tft.h
	gcc -Os -c tft.c

tft_init.o: tft_init.c 
	gcc -Os -c tft_init.c
	
ST7789.o: ST7789.c ST7789.h
	gcc -Os -c ST7789.c

bmp.o: bmp.c bmp.h ST7789.h
	gcc -Os -c bmp.c

clean:
	rm -rf *o tft_init

