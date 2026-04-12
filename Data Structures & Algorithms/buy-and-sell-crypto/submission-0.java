class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int sell = 0;
        int profit = 0;
        for(int i = 0; i < prices.length; i++){
            for(int j = i; j < prices.length; j++){
                if((prices[j] - prices[i]) > profit){
                    profit = prices[j] - prices[i];
                    buy = i;
                    sell = j;
                }
            }
        }

        System.out.println(buy);
        System.out.println(sell);

        return profit;
    }
}
