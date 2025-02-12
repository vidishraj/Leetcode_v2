class Solution {
public boolean winnerOfGame(String colors) {
		int aliceWins=0;
		int bobWins=0;
		int aliceCq=0;
		int bobCq=0;
		for(int i=0;i<colors.length();i++) {
			if(colors.charAt(i)=='A') {
				if(bobCq>=3) {
					bobWins+=bobCq-2;
				}
				bobCq=0;
				aliceCq++;	
			}
			if(colors.charAt(i)=='B'){
				if(aliceCq>=3) {
					aliceWins+=aliceCq-2;
				}
				aliceCq=0;
				bobCq++;
			}
		}
		if(bobCq>=3) {
			bobWins+=bobCq-2;
		}
		if(aliceCq>=3) {
			aliceWins+=aliceCq-2;
		}
		if(aliceWins>bobWins){
			return true;
		}
		return false;
	 }
}