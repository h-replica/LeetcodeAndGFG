
// class Solution {
//     public String reorganizeString(String s) {
        
//         // corner case
//         if(s.length() == 0 || s == null){
//             return "";
//         }
        
//         // parse the char and frequency in s
//         Map<Character, Integer> dict = new HashMap<>();
//         for(char c : s.toCharArray()){
//             dict.put(c, dict.getOrDefault(c, 0) + 1);
//         }
        
//         // put each c into pq
//         PriorityQueue<Character> pq = new PriorityQueue<>((i1, i2) -> (dict.get(i2) - dict.get(i1)));
//         for(char c : dict.keySet()){
//             pq.add(c);
//         }
        
//         // traverse pq
//         StringBuilder sb = new StringBuilder();
//         char first_char = ' ', second_char = ' ';
//         int first_freq = 0, second_freq = 0;
//         // every time we pair up two elements
//         while(pq.size() > 1){
//             first_char = pq.poll();
//             first_freq = dict.get(first_char);
//             second_char = pq.poll();
//             second_freq = dict.get(second_char);
            
//             sb.append(first_char);
//             first_freq--;
//             sb.append(second_char);
//             second_freq--;
            
//             // put back
//             if(first_freq > 0){
//                 dict.put(first_char, first_freq);
//                 pq.add(first_char);
//             }
            
//             if(second_freq > 0){
//                 dict.put(second_char, second_freq);
//                 pq.add(second_char);
//             }
//         }
        
//         // if single element remain in pq, check if freq is 1
//         if(pq.size() == 1){
//             if(dict.get(pq.peek()) > 1){
//                 return "";
//             }
//             else{
//                 sb.append(pq.poll());
//             }
//         }
        
//         return sb.toString();
        
//     }}

import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public String reorganizeString(String s) {
        if(s.length() == 0 || s == null) return "" ;
        Map<Character , Integer> freq = new HashMap<>();
        
        for(char c : s.toCharArray()){
            freq.put(c , freq.getOrDefault( c, 0)+1) ;
        }
        System.out.println(freq);
        PriorityQueue<Character> pq = new PriorityQueue<>((i , j) -> (freq.get(j) - freq.get(i)) );
        for(char c : freq.keySet()) pq.add(c) ;
        System.out.println(pq);
        StringBuilder sb = new StringBuilder() ;
        char fir =' ', sec=' ' ;
        int ff=0 , sf=0 ;
        while(pq.size() > 1) {

            fir = pq.poll() ;
            ff = freq.get(fir) ;

            sec = pq.poll();
            sf = freq.get(sec) ;

            sb.append(fir) ;
            sb.append(sec) ;

            ff-- ;
            sf--;

            if(ff>0){
            freq.put(fir , ff) ;
            pq.add(fir) ;
            }

            if(sf>0){
                freq.put(sec , sf) ;
                pq.add(sec) ;
                }
            
        }

        if(pq.size() > 0){

            if(freq.get(pq.peek())>1) return "" ;
            sb.append(pq.poll()) ; 
        }

        return sb.toString() ;

        
    }
}