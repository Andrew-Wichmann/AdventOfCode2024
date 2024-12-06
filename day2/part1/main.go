package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func assert_sign(diffs []int) (bool, int) {
	var negative bool
	var found bool
	for _, diff := range diffs {
		if diff < 0 {
			negative = true
			found = true
			continue
		} else if diff > 0 {
			negative = false
			found = true
			continue
		}
	}
	if found == false {
		return false, -1
	}
	bad_level := -1
	if negative {
		for i, diff := range diffs {
			if diff >= 0 {
				if bad_level != -1 {
					return false, bad_level
				} else {
					bad_level = i
				}
			}
		}
	} else {
		for i, diff := range diffs {
			if diff <= 0 {
				if bad_level != -1 {
					return false, bad_level
				} else {
					bad_level = i
				}
			}
		}
	}
	return true, bad_level
}
func assert_in_range(diffs []int, bad_level int) bool {
	for i, diff := range diffs {
		if math.Abs(float64(diff)) > 3 || math.Abs(float64(diff)) < 1 {
			if i != bad_level {
				return false
			}
		}
	}
	return true
}

func main() {
	data, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}
	count := 0
	for i, line := range strings.Split(string(data), "\n") {
		if line == "" {
			continue
		}
		levels := strings.Split(line, " ")
		level_ints := []int{}
		for _, level := range levels {
			i, err := strconv.Atoi(level)
			if err != nil {
				panic(err)
			}
			level_ints = append(level_ints, i)
		}
		diffs := []int{}
		for j := range level_ints {
			if j == len(level_ints)-1 {
				continue
			}
			diffs = append(diffs, level_ints[j+1]-level_ints[j])
		}
		check, blu := assert_sign(diffs)
		if check {
			if assert_in_range(diffs, blu) {
				count += 1
				fmt.Printf("safe %d: %v diffs: %v\n", i, level_ints, diffs)
			} else {
				fmt.Printf("Not in range %d: %v diffs: %v\n", i, level_ints, diffs)
			}
		} else {
			fmt.Printf("Not inc/dec %d: %v diffs: %v\n", i, level_ints, diffs)
		}
	}
	fmt.Printf("safe count: %d", count)
}
