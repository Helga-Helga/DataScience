#include <stdlib.h>
#include <stdio.h>

#include "main.h"

Array *createArray(unsigned int size) {
  Array *a = (Array*)malloc(sizeof(Array));
  a->size = size;
  a->data = (double*)malloc(sizeof(double)*size);
  return a;
}

int destroyArray(Array *array) {
  free(array->data);
  free(array);
  return 0;
}

int fillArray(Array *array) {
  int i = array->size;
  while (i-- > 0) {
    array->data[i] = (double)rand()/RAND_MAX;
  }
}

int displayArray(Array *array) {
  unsigned int i = array->size;
  while (i-- > 0) {
    printf("%f\n", array->data[i]);
  }
}

double multiplyArrays(Array *a, Array *b) {
  if (a == NULL || b == NULL) {
    return 0;
  }
  if (a->size != b->size) {
    return 0;
  }
  unsigned int i = a->size;
  double c = 0;
  while (i-- > 0) {
    c += (a->data[i])*(b->data[i]);
  }
  return c;
}

int main() {
  Array *array_1 = createArray(5);
  Array *array_2 = createArray(5);
  fillArray(array_1);
  fillArray(array_2);
  printf("%s\n", "First array");
  displayArray(array_1);
  printf("%s\n", "Second array");
  displayArray(array_2);
  double result;
  result = multiplyArrays(array_1, array_2);
  printf("%s\n", "Result");
  printf("%f\n", result);
  destroyArray(array_1);
  destroyArray(array_2);
}
