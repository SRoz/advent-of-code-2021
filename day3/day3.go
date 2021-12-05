package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func ReadInp(r io.Reader) ([][]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	var result [][]int

	for scanner.Scan() {
		line := []int{}
		for _, char := range scanner.Text() {
			line = append(line, int(char-'0'))
		}
		result = append(result, line)
	}
	return result, scanner.Err()
}

func Power(x int, y int) int {
	if y == 0 {
		return 1
	}
	result := x
	for i := 1; i < y; i++ {
		result = result * x
	}
	return result
}

func BinaryToDecimal(binary []int) int {
	result := 0
	size := len(binary)
	for i := 0; i < size; i++ {
		result += (binary[size-i-1] * Power(2, i))
	}
	return result
}

func Part1(inputs [][]int) {

	array_size := len(inputs[0])

	// Counters for 0 and 1
	zero_counts := make([]int, array_size)
	one_counts := make([]int, array_size)

	for i := 0; i < array_size; i++ {
		zero_counts[i] = 0
		one_counts[i] = 0
	}

	// Loop through and count
	for _, line := range inputs {
		for idx, num := range line {
			zero_counts[idx] += (1 - num)
			one_counts[idx] += num
		}
	}

	gamma := make([]int, array_size)
	epsilon := make([]int, array_size)
	//Comparisons
	for idx, _ := range zero_counts {
		if zero_counts[idx] < one_counts[idx] {
			gamma[idx] = 1
			epsilon[idx] = 0
		} else {
			gamma[idx] = 0
			epsilon[idx] = 1
		}
	}

	fmt.Println(BinaryToDecimal(gamma) * BinaryToDecimal(epsilon))

}

func main() {
	file, _ := os.Open("day3/inputs/input1.txt")
	inputs, _ := ReadInp(file)
	Part1(inputs)
}
