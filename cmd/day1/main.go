package main

import (
	"advent-of-code-2021/internal/converters"
	"advent-of-code-2021/internal/files"
	"log"
)

func HigherOrLower(first int, second int) bool {
	return second > first
}

func CountBoolIf(condition bool) func(bool) int {
	count := 0

	return func(result bool) int {
		if condition == result {
			count++
		}

		return count
	}
}

func main() {
	var err error

	defer func() {
		if err != nil {
			log.Fatalf("%+v", err)
		}
	}()

	rawInput, err := files.Load("cmd/day1/input.txt", "\n")
	if err != nil {
		return
	}

	depths, err := converters.StringsToInts(rawInput...)
	if err != nil {
		return
	}

	counter := CountBoolIf(true)

	count := 0
	for i := 0; i < len(depths) - 1; i++ {
		count = counter(HigherOrLower(depths[i], depths[i+1]))
	}
	print(count)
}
