package WebHandling;

public class tryProgs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(expandString("2ad3b4c"));
		System.out.println(expandString("2a3b4c"));
		System.out.println(expandString("2ab3b4c"));
	}
	public static String expandString(String input)
	{
        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < input.length()) {
            if (Character.isDigit(input.charAt(i))) {
                int count = Character.getNumericValue(input.charAt(i));
                i++;
                StringBuilder group = new StringBuilder();
                while (i < input.length() && !Character.isDigit(input.charAt(i))) {
                    group.append(input.charAt(i));
                    i++;
                }
                result.append(group.toString().repeat(count));
            } else {
                result.append(input.charAt(i));
                i++;
            }
        }
        return result.toString();
}
}

adadbbbcccc
aabbbcccc
ababbbbcccc
