import java.util.ArrayList;

class Solution {
    public String intToRoman(int num) {
        ArrayList<String> numbers = new ArrayList<String>();
        int position = 1; // Position like Ones place, Tens place, Hundreds place, etc.
        int digit, i = 0;
        String s = "";
        while(num != 0){
            digit = num % 10;
            
            // The 6 Special Cases
            
            if(digit == 4 && position == 1) {
            	numbers.add("IV");
            }
            else if(digit == 9 && position == 1) {
            	numbers.add("IX");
            }
            else if(digit == 4 && position == 2) {
            	numbers.add("XL");
            }
            else if(digit == 9 && position == 2) {
            	numbers.add("XC");
            }
            else if(digit == 4 && position == 3) {
            	numbers.add("CD");
            }
            else if(digit == 9 && position == 3) {
            	numbers.add("CM");
            }
            
            // Rest of the numbers, since it's all 0-3 , 4 , 5-8, 9, we modify the roman numerals based on the position of the digit
            // Need to re-initialise String s or it will carry over the roman numeral of the previous digit
            
            else if(digit <= 3 && position == 1) {
            	s = "";
            	for(i=0;i<digit;i++) {
            		s += "I";
            	}
            	numbers.add(s);
            }
            else if(5<= digit && digit <= 8 && position == 1) {
            	s = "V";
            	for(i=0;i<digit-5;i++) {
            		s += "I";
            	}
            	numbers.add(s);
            }
            else if(digit <= 3 && position == 2) {
            	s = "";
            	for(i=0;i<digit;i++) {
            		s += "X";
            	}
            	numbers.add(s);
            }
            else if(5<= digit && digit <= 8 && position == 2) {
            	s = "L";
            	for(i=0;i<digit-5;i++) {
            		s += "X";
            	}
            	numbers.add(s);
            }
            else if(digit <= 3 && position == 3) {
            	s = "";
            	for(i=0;i<digit;i++) {
            		s += "C";
            	}
            	numbers.add(s);
            }
            else if(5<= digit && digit <= 8 && position == 3) {
            	s = "D";
            	for(i=0;i<digit-5;i++) {
            		s += "C";
            	}
            	numbers.add(s);
            }
            else if(digit <= 3 && position == 4) {
            	s = "";
            	for(i=0;i<digit;i++) {
            		s += "M";
            	}
            	numbers.add(s);
            }
            // This question assume 1 <= num <= 3999  
            num -= digit;
            num /= 10;
            position++;
        }
        // The ArrayList is now [Ones place, Tens place, Hundreds place...]
        // For loop from the back to get the largest number at the front of return string
        s = "";
        for(i=numbers.size()-1;i>=0;i--) {
        	s += numbers.get(i);
        }
        return s;
    }
}