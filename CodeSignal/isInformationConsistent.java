boolean isInformationConsistent(int[][] evidences) {

    // iterate the columns of the evidences
    for (int j = 0; j < evidences[0].length; j++) {

        // set the flag for innocent and guilty
        boolean innocent = false, guilty = false;

        // iterate the rows of the evidences
        for (int i = 0; i < evidences.length; i++) {

            switch (evidences[i][j]) {
                // if the row contains -1 there exists an innocent
                case -1:
                    innocent = true;
                    break;
                // if the row contains 1 there exists an guilty
                case 1:
                    guilty = true;
                    break;
            }
        }
        // return false if the evidence is both guilty and innocent at the same time
        if (innocent && guilty) {
            return false;
        }
    }
    // return true if the rows are either innocent or guilty
    return true;
}