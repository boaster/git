
//
//	vuln in size returned by snprintf
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct {

  size_t      prev_size;  /* Size of previous chunk (if free).  */
  size_t      size;       /* Size in bytes, including overhead. */

  struct malloc_chunk* fd;         /* double links -- used only if free. */
  struct malloc_chunk* bk;

} malloc_chunk, *pmalloc_chunk;

typedef struct {
	int prev_size;
	int size;
	int next_prev_size;
	int next_size;
} smetadata, *psmetadata;

char  		big_buf[0x400];
char  		keystream[80];
psmetadata 	metadatas[12];
char  		ciphertext[0x400];
char* 		messages_array[12];
int   		sizes_array[12];


int read_input(char* inBuffer, int size, char delim) {
	char inChar;
	int i = 0;
	int x;
	for (i ; i < (size-1); i++) {
		x = read(0, &inChar, 1);
		if (x != 1 || inChar == '\n') {
			break;
		}
		*inBuffer = inChar;
		++inBuffer;
	}
	inBuffer[i] = 0;
	return i;
}

void print_welcome(char* outBuffer) {
	printf("\n\tHey Guy %s\n", outBuffer);
}

int read_int32() {
	char inBuffer[40];
	read_input(inBuffer, 0x20, '\n');
	return atoi(inBuffer);
}

int get_choice(void) {
	return read_int32();
}

void save_metadata(char* message, int z) {

	pmalloc_chunk p = (*(pmalloc_chunk*)&message)-0x10;
	pmalloc_chunk next_chunk = p + p->size;

	int prev_size = p->prev_size;
	int size = p->size;
	int next_prev_size = next_chunk->prev_size;
	int next_size = next_chunk->size;

	metadatas[z]->prev_size = prev_size;
	metadatas[z]->size = size;
	metadatas[z]->next_prev_size = next_prev_size;
	metadatas[z]->next_size = next_size;
}

int verify_chunk(void* message, int x) {
	pmalloc_chunk p = (*(pmalloc_chunk*)&message)-0x10;
	pmalloc_chunk next_chunk = p + p->size;

	int prev_size = p->prev_size;
	int size = p->size;
	int next_prev_size = next_chunk->prev_size;
	int next_size = next_chunk->size;

	if (metadatas[x]->prev_size == prev_size && 
		metadatas[x]->size == size && 
		metadatas[x]->next_prev_size == next_prev_size &&
		metadatas[x]->next_size == next_size)
	{
		return 1;
	}
	else {
		return 0;
	}
}

void encrypt_msg(char* name) {
	int idx = read_int32();
	if (idx < 0 || idx > 11 || messages_array[idx] == 0) {
		exit(0);
	}

//	rabbit_keystream(keystream, name);	// probably gen keystream
	memset(big_buf,   0, 0x400);
	memset(ciphertext, 0, 0x400);
//	rabbit_encrypt(&keystream, messages_array[idx], &ciphertext, sizes_array[idx]); // probably encrypt
	write(1, ciphertext, sizes_array[idx]);
	printf("OVE\n");

}

void update_name(char* name) {
	read_input(name, 0x100, '\n');
	print_welcome(name);
}

int edit_message(void) {
	int idx = read_int32();
	if (idx < 0 || idx > 11 || messages_array[idx] == 0) {
		exit(0);
	}

	int size = read_int32();
	if (size > sizes_array[idx] || size <= 0) {
		exit(0);
	}

	return read_input(messages_array[idx], size, '\n');
}

void create_msg(void) {
	char* msg2 = malloc(0x400);
	char frmt[0x32];
	memcpy(frmt, "B1U3L04usMSG  [xD:%s @ %d! %s", 0x32);

	for (int i = 0; i < 12; i++) {
		if (messages_array[i] == 0) {
			char msg1[0x80];
			read_input(msg1, 0x80, '\n');
			read_input(msg2, 0x180, '\n');
			int y = read_int32();
			char full_msg[0x200];
			int num_converted = snprintf(full_msg, 0x200, frmt, msg1, y, msg2);
			free(msg2);
			printf("VEW%s\n", full_msg);
			for (int x = 0; x < 12; x++) {
				if (messages_array[x] != 0) {
					if(verify_chunk(messages_array[x], x) != 1) {
						puts("******error:double free or corruption (heap)");
						exit(-1);
					}
				}
			}
			messages_array[i] = malloc(0x200);
			memset(messages_array[i], 0, 0x200);
			for (int z = 0; z < 12; z++) {
				if (messages_array[z] != 0) {
					save_metadata(messages_array[z], z);
				}
			}
			sizes_array[i] = num_converted;
			memcpy(messages_array[i], full_msg, num_converted);
			printf("%d\n", i);
			return;
		}
	}
	exit(0);
}

void delete_msg(void) {
	int idx = read_int32();
	if (idx < 0 || idx > 11) {
		exit(0);
	}
	char* ptr = messages_array[idx];
	if (ptr != 0) {
		for (int i = 0; i < 12; i++) {
			if (messages_array[i] != 0) {
				if (verify_chunk(messages_array[i], i) != 1) {
					puts("******error:double free or corruption (heap)");
					exit(-1);
				}
			}
		}
		free(ptr);
		messages_array[idx] = 0;
		sizes_array[idx] = 0;
		for (int x = 0; x < 12; x++) {
			if (messages_array[x] != 0) {
				save_metadata(messages_array[x], x);
			}
		}
	}
}


int main(void) {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

	char name[0x100];
	memset(name, 0, 0x100);

	read_input(name, 0x100, '\n');
	print_welcome(name);


	while (1) {
		int choice = get_choice();
		switch (choice) {
			case 1:
				create_msg();
				break;
			case 9:
				return 0;
			case 23:
				encrypt_msg(name);	// incomplete
				break;
			case 44:
				delete_msg();
				break;
			case 36854:
				edit_message();
				break;
			case 808080:
				update_name(name);
				break;
			default:
				puts("ERR");
				break;
		}
	}

	return 0;
}
