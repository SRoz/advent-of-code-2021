package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func Reader(r io.Reader) ([]string, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	var result []string
	for scanner.Scan() {
		x := scanner.Text()
		result = append(result, x)
	}
	return result, scanner.Err()
}

// Part 1
func MoveSubmarine(starting_position [2]int, instruction string) [2]int {
	instruction_vector := strings.Fields(instruction)
	direction := instruction_vector[0]
	units, _ := strconv.Atoi(instruction_vector[1])

	var output [2]int
	if direction == "forward" {
		output[0], output[1] = starting_position[0]+units, starting_position[1]
	} else if direction == "up" {
		output[0], output[1] = starting_position[0], starting_position[1]-units
	} else if direction == "down" {
		output[0], output[1] = starting_position[0], starting_position[1]+units
	}

	return output
}

// Part 2
func MoveSubmarinePart2(starting_position [3]int, instruction string) [3]int {
	instruction_vector := strings.Fields(instruction)
	direction := instruction_vector[0]
	units, _ := strconv.Atoi(instruction_vector[1])

	output := starting_position

	if direction == "forward" {
		output[0] = starting_position[0] + units
		output[1] = starting_position[1] + starting_position[2]*units
	} else if direction == "up" {
		output[2] = starting_position[2] - units
	} else if direction == "down" {
		output[2] = starting_position[2] + units
	}

	return output
}

func main() {
	file, _ := os.Open("day2/inputs/input1.txt")
	input, _ := Reader(file)

	// Part 1
	position := [2]int{0, 0} //start at 0,0

	for _, instruction := range input {
		position = MoveSubmarine(position, instruction)
	}

	fmt.Println(position)
	fmt.Println(position[0] * position[1])

	//Part 2
	position2 := [3]int{0, 0, 0} //start at 0,0,0, (x,y,aim)

	for _, instruction := range input {
		position2 = MoveSubmarinePart2(position2, instruction)
	}

	fmt.Println(position2)
	fmt.Println(position2[0] * position2[1])

}
