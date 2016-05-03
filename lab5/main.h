struct Array {
  double *data;
  unsigned int size;
};

typedef struct Array Array;

Array* createArray(unsigned int size);
int destroyArray(Array *array);
int fillArray(Array *array);
int displayArray(Array *array);
double multiplyArrays(Array *a, Array *b);
