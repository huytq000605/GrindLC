package main

/*
First we calculate a prefix sum array

*/

// Vietnamese
/*
Lập 1 mảng prefix tổng
Hàm maxSum nhận vào mảng prefix tổng phía trên và độ dài m và n cho 2 substring, hàm sẽ luôn giả sử substring có độ dài m đứng trước substring có độ dài n, ta khởi tạo giá trị ban đầu cho chuỗi độ dài m chính là prefixSum[m-1] và tổng độ dài 2 chuỗi
Cho vòng lặp đi qua prefix, ta luôn đảm bảo được 2 mảng con không bao giờ đè lên nhau vì index mảng length m bị chặn trên tại i-n cũng như index mảng length n bị chặn dưới bởi i-n
*/
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) int {
	prefixSum := make([]int, len(nums))
	for idx, num := range nums {
		if idx == 0 {
			prefixSum[idx] = num
			continue
		}
		prefixSum[idx] = prefixSum[idx-1] + num
	}
	res1 := maxSum(prefixSum, firstLen, secondLen)
	res2 := maxSum(prefixSum, secondLen, firstLen)
	if res1 > res2 {
		return res1
	}
	return res2
}

func maxSum(prefix []int, m int, n int) int {
	// Khởi tạo giá trị ban đầu với m và n là vị trí đầu tiên thoả mãn
	maxFirst := prefix[m-1]
	// Trick: Dùng tổng để đảm bảo 2 subarray không đè lên nhau
	bothMax := prefix[m+n-1] - prefix[m-1] + maxFirst
	for i := m + n; i < len(prefix); i++ {
		first := prefix[i-n] - prefix[i-n-m]
		if first > maxFirst {
			maxFirst = first
		}
		both := prefix[i] - prefix[i-n] + maxFirst
		if both > bothMax {
			bothMax = both
		}
	}

	return bothMax
}
