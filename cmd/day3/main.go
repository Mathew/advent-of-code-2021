package main

import (
	"advent-of-code-2021/internal/converters"
	"advent-of-code-2021/internal/counters"
	"advent-of-code-2021/internal/files"
	"log"
	"strings"
)

type PowerMonitor struct {
	readings [][]string
}

func (pm *PowerMonitor) PowerRate() (int64, error) {
	var gammaRate []string
	var episilonRate []string
	for i := 0; i < len(pm.readings[0]); i++ {
		sc := counters.NewStringCounter()
		for j := 0; j < len(pm.readings); j++ {
			sc.Count(pm.readings[j][i])
		}
		results := sc.Sorted()
		gammaRate = append(gammaRate, results[0])
		episilonRate = append(episilonRate, results[1])
	}

	gamma, err := converters.BinaryToInt(gammaRate...)
	if err != nil {
		return 0, err
	}
	episilon, err := converters.BinaryToInt(episilonRate...)
	if err != nil {
		return 0, err
	}

	return gamma * episilon, nil
}

func NewPowerMonitor(readings []string) PowerMonitor {
	return PowerMonitor{
		converters.TwoDimArrayFromString(
			strings.Join(readings, ""),
			len(readings[0]),
		),
	}
}

func main() {
	var err error

	defer func() {
		if err != nil {
			log.Fatalf("%+v", err)
		}
	}()

	rawBinary, err := files.Load("cmd/day3/input.txt", "\n")
	if err != nil {
		return
	}

	powerMonitor := NewPowerMonitor(rawBinary)
	rate, err := powerMonitor.PowerRate()
	if err != nil {
		return
	}

	log.Printf("Part One: Power Consumption Rate; %d", rate)
}
