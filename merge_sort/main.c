#include <stdio.h>

void print_array(int a[], size_t size) {
	int i=0;
	for(int i=0; i<size; i++) {
		printf("%d\n", a[i]);
	}
}

void merge_sort(int a[]) {

}

int main() {
	int a[] = {3,4,6,2,5,7,1,3,5,7,4,2,4,9};
	size_t size = sizeof(a) / sizeof(a[0]);

	printf("--- Merge Sort ---\n");
	print_array(a, size);
}
