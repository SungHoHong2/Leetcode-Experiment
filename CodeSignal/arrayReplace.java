
int[] arrayReplace(int[] inputArray, int elemToReplace, int substitutionElem) {
    // iterate the numbers
    for (int i = 0; i < inputArray.length; i++) {
        // if the
        if (inputArray[i] == elemToReplace)
            inputArray[i] = substitutionElem;
        }
    return inputArray;
}