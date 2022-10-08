class Solution {
    public int romanToInt(String s) {
        int solution = 0;
        char digit, nextdigit;
        for(int i = 0; i< s.length(); i++){
            digit = s.charAt(i);
            
            // Need to check the next digit for the 6 subtraction cases
            if(i<s.length() - 1){ // to prevent out of bounds error
            nextdigit = s.charAt(i+1);
            if(digit == 'I' && nextdigit == 'V'){
                i++;
                solution += 4;
                continue;
            }
            else if(digit == 'I' && nextdigit == 'X'){
                i++;
                solution += 9;
                continue;
            }
            else if(digit == 'X' && nextdigit == 'L'){
                i++;
                solution += 40;
                continue;
            }
            else if(digit == 'X' && nextdigit == 'C'){
                i++;
                solution += 90;
                continue;
            }
            else if(digit == 'C' && nextdigit == 'D'){
                i++;
                solution += 400;
                continue;
            }
            else if(digit == 'C' && nextdigit == 'M'){
                i++;
                solution += 900;
                continue;
            }
            }
            
            switch(digit){
            case 'I':
                solution += 1;
                break;
            case 'V':
                solution += 5;
                break;
            case 'X':
                solution += 10;
                break;
            case 'L':
                solution += 50;
                break;
            case 'C':
                solution += 100;
                break;
            case 'D':
                solution += 500;
                break;
             case 'M':
                solution += 1000;
                break;
            }
        }
    
        return solution;
}
}
