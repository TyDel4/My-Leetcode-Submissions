class Solution {
    public int[] plusOne(int[] digits) {
        boolean carryOver = true;

        for (int i = digits.length - 1; i >= 0 && carryOver; i--) {
            if (digits[i] >= 9) {
                digits[i] = 0;
            } else {
                digits[i] += 1;
                carryOver = false;
            }
        }
        
        if (carryOver) {
            int[] newArray = new int[digits.length + 1];

            // Add the element at the front
            newArray[0] = 1;

            // Copy the original array to the new array
            System.arraycopy(digits, 0, newArray, 1, digits.length);
            
            return newArray;
        }

        return digits;
    }
}