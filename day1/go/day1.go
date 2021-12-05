package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

// ReadInts reads whitespace-separated ints from r. If there's an error, it
// returns the ints successfully read so far as well as the error value.
// Borrowed from https://stackoverflow.com/questions/9862443/golang-is-there-a-better-way-read-a-file-of-integers-into-an-array
func ReadInts(r io.Reader) ([]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanWords)
	var result []int
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}

// Part 1
func CountIncreases(numbers []int) {
	num_increases := 0
	for idx, _ := range numbers {
		if idx == 0 {
			continue
		}
		if numbers[idx] > numbers[idx-1] {
			num_increases++
		}
	}
	fmt.Println("Num increases: ", num_increases)
}

// Part 2
func Sum(array []int) int {
	result := 0
	for i := 0; i < len(array); i++ {
		result += array[i]
	}
	return result
}

func SlidingWindow(numbers []int, window_size int) {

	window_sums := []int{}

	for idx, _ := range numbers {
		if idx < window_size-1 {
			continue
		}

		slice := numbers[(idx - window_size + 1):(idx + 1)]

		window_sums = append(window_sums, Sum(slice))

	}
	CountIncreases(window_sums)
}

func main() {
	// Read in data
	file, _ := os.Open("day1/inputs/input1.txt")
	ints, _ := ReadInts(file)

	// Q1
	CountIncreases(ints)

	// Q2
	SlidingWindow(ints, 3)

}
