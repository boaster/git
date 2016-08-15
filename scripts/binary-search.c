#include <stdio.h>

int binarySearch(int *alist, int item, int len)
{
	int first = 0;
	int last = len-1;
	int found = 0;

	while ((first <= last) && (!found) ){
		int mid = (first + last) / 2;
		if (alist[mid] == item){
			found = 1;
		}
		else {
			if (item < alist[mid]){
				last = mid-1;
			}
			else {
				first = mid+1;
			}
		}
	}
	return found;
}

int main(int argc, char* argv[])
{
	int intArray[] = {1, 3, 6, 13, 15, 17, 21, 24, 26, 31, 33, 37, 41, 46, 47};
	int arrayLen = sizeof(intArray) / sizeof(int);
	if ( binarySearch(intArray, 17, arrayLen) ){
		printf("Found!\n");
	}
	else {
		printf("Not found.\n");
	}
	return 0;
}