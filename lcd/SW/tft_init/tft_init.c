/*##############################################################*/
/*    Reimar Barnstorf www.7soft.de                             */
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

	if (!bcm2835_init())
	return 1;


	TFT_init_board();
	TFT_hard_reset();
	STcontroller_init();
	
	TFT_SetBacklightPWMValue( 255 );

   	return 0;
}

