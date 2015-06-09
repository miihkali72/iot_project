/*##############################################################*/
/*   Reimar Barnstorf www.7soft.de                              */
/*##############################################################*/

#include <bcm2835.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include "tft.h"
#include "ST7789.h"
#include "bmp.h"


int main( int argc, char *argv[] )
{
        uint16_t picture[1][ PICTURE_PIXELS ];

        if (!bcm2835_init())
        {
        printf("init failed!!! \n");
        return 1;
        }

        // depict a BMP file
        // ---------------------------------------------
        printf("File : %s \n", argv[1]);
        
        Read_bmp2memory ( argv[1], &picture[0][ PICTURE_PIXELS-1 ] );
        STcontroller_Write_Picture ( &picture[0][0], PICTURE_PIXELS );

   	return 0;
}

