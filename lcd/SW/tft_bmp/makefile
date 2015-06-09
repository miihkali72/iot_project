all: tft_bmp

tft_bmp: tft_bmp.o tft.o ST7789.o bmp.o
	gcc tft_bmp.o tft.o ST7789.o bmp.o -lbcm2835 -lrt -o tft_bmp

tft.o: tft.c tft.h
	gcc -Os -c tft.c

tft_bmp.o: tft_bmp.c 
	gcc -Os -c tft_bmp.c
	
ST7789.o: ST7789.c ST7789.h
	gcc -Os -c ST7789.c

bmp.o: bmp.c bmp.h ST7789.h
	gcc -Os -c bmp.c

clean:
	rm -rf *o tft_bmp

