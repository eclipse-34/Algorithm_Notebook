import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int i = 0; i < commands.length; i++) {
            int[] list = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
            Arrays.sort(list);
            System.out.println(Arrays.toString(list));
            answer[i] = list[commands[i][2] - 1];
        }
        
        return answer;
    }
}