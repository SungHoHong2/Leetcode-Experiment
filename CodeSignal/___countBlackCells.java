int countBlackCells(int n, int m) {
    //
    int div = 1;
    //
    for (int i = 1; i <= n; i++) {

        if (n % i == 0 && m % i == 0)
            div = i;
    }

    return n + m + div - 2;
}