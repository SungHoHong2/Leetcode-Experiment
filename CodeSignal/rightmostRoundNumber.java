int rightmostRoundNumber(int[] inputArray) {
    // set the index
    int index = 0;
    // iterate the numbers from the right
    for (int i = inputArray.length - 1; i >= 0; i--){
        // return the index of the number if it divides by 10
        if(inputArray[i]%10==0)
            return i;
    }
    // return -1 if it fails
    return -1;
}