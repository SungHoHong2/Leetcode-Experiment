"""
valid time
"""

boolean validTime(String time){

    // create a internal class
    class Helper {
        int charToInt(char symbol)
        {
            return symbol - '0';
        }
    }

    // invoke the helper function
    Helper h = new Helper();

    // compute the number of hours
    int hours = h.charToInt(time.charAt(0)) * 10 + h.charToInt(time.charAt(1));

    // compute the number of minutes
    int minutes = h.charToInt(time.charAt(3)) * 10 + h.charToInt(time.charAt(4));

    // return true if the hours and minutes are within the valid time
    if(hours<24&&minutes<60){
        return true;
    }

    // return false if the hours and minutes are not in the valid time
    return false;
}
