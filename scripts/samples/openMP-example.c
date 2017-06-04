#include <omp.h>
#include <stdio.h>
#include <openssl/md5.h>
#include <string.h>

/* guilt
* 1. Args password and a number of iterations.
*
* 2. md5 bug
*
* Openmp program that would spawn worker threads
*
* This program reads passwords from stdin and takes an optional arguments
* to specify the max number of iterations you want to try. It defaults
* to 20 if non given.
*
* Usage: 
* $ gcc bf.c -lssl -fopenmp -lcrypto -o bf
* $ crunch 1 6 abcdefghijklmnopqrstuvwxyz1234567890 | ./bf 20
*
*/


unsigned char get_next_word(unsigned char * buf);

main (int argc, char** argv)  {

int n, nthreads, tid,a,b;
MD5_CTX c;
unsigned char input[16];
unsigned char buffer[16];
unsigned char strbuffer[33];
volatile unsigned char finished;
finished = 0;
unsigned long byte_counter = 0;
unsigned int MB_counter = 0;
unsigned int prev_MB_counter = 0;

b = 20;
if (argc > 1) b = atoi(argv[1]);


/* Fork a team of threads with each thread having a private tid variable */
#pragma omp parallel private(tid,c,buffer,strbuffer,n, input,a) shared(finished, byte_counter,b,MB_counter,prev_MB_counter)
  {
	  /* Obtain and print thread id */
	  tid = omp_get_thread_num();
	  /* Only master thread does this */
	  if (tid == 0) 
	    {
	    nthreads = omp_get_num_threads();
	    printf("Number of threads = %d\n", nthreads);
	    }
	  while (finished == 0) {
		  MD5_Init(&c);
		  finished = get_next_word(input);
		  #pragma omp atomic
		  byte_counter += strlen(input)+1;

		  for (a=1 ; a < b ; a++){
			  MD5_Update(&c,input,strlen(input));
			  MD5_Final(buffer,&c);
			  for (n = 0; n< 16; ++n) {
			    snprintf(&(strbuffer[n*2]), 3, "%02x", buffer[n]);
			  }
			 
			  if (! strcmp(strbuffer,"xxxxxxxxxxxxx")) {
				printf("\nmatch found! %s with %d iterations %s\n", input,a,strbuffer);
				finished = 1;
			  }
		  }
		  if (tid == 0){
			MB_counter = byte_counter >> 20;
			if (MB_counter != prev_MB_counter) {
				printf("\rProcessed %d MB of data so far", MB_counter );
				fflush(stdout);
				prev_MB_counter = MB_counter;
			}
		  }
	  }
	  if (tid == 0) printf("\n\nComputation finished!\n\n");
  }
  /* All threads join master thread and terminate */

}

unsigned char get_next_word(unsigned char * buf){
	int ret = 0;
	#pragma omp critical(read_from_stdin)
	{
		ret = scanf("%15s", buf);
	}
	if (ret == -1){
		return 1;
	} else{
		return 0;
	}
}
	
