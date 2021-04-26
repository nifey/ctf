#include<stdio.h>
#include<stdlib.h>
int main() {
	srand(0x1337);
	printf("rand_numbers = [");
	for (int i=0; i<67; i++) {
		printf("0x%x, ", rand());
	}
	printf("0x%x]", rand());
}
