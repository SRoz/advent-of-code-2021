package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func ReadInts(r io.Reader) ([]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	var result []int

	// Get lines from file
	var input string
	for scanner.Scan() {
		input = scanner.Text()
	}

	string_array := strings.Split(input, ",")

	for _, num := range string_array {
		num_int, _ := strconv.Atoi(num)
		result = append(result, num_int)
	}
	return result, scanner.Err()
}

func LanternFish(fishes []int, num_days int) {

	// Create input vec: number of fishies across the 9 possible states
	n_fishies := [9]int{}
	for _, state := range fishes {
		n_fishies[state]++
	}

	for i := 0; i < num_days; i++ {
		fishies_out := [9]int{0}

		// Move all fishies down a state
		for j := 1; j < 9; j++ {
			fishies_out[j-1] = n_fishies[j]
		}

		// Put fishies ready to pop into two buckets
		fishies_out[6] += n_fishies[0]
		fishies_out[8] += n_fishies[0]

		n_fishies = fishies_out
	}

	// Count total fishies
	sum_fishies := 0
	for _, n := range n_fishies {
		sum_fishies += n
	}
	fmt.Printf("After %v days, there are %v lantern fishies\n", num_days, sum_fishies)

}

func main() {
	file, _ := os.Open("day6/inputs/input1.txt")
	input, _ := ReadInts(file)

	LanternFish(input, 80)
	LanternFish(input, 256)
}
