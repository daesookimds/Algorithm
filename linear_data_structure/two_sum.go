package main

func main() {
	var nums = []int{2, 7, 11, 13}
	var target = 9
	var result = twoSum(nums, target)

	println(result[0], result[1])
}

func twoSum(nums []int, target int) []int {
	numsMap := make(map[int]int)
	for i, num := range nums {
		numsMap[num] = i
	}

	for i, num := range nums {
		if j, ok := numsMap[target-num]; ok && i != j {
			return []int{i, j}
		}
	}
	return []int{}
}
