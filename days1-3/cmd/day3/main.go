package main

import (
	"advent-of-code-2021/internal/converters"
	"advent-of-code-2021/internal/counters"
	"advent-of-code-2021/internal/files"
	"advent-of-code-2021/internal/structures"
	"log"
	"strings"
)

type Diagnostic func(DiagnosticReporter) (int64, error)

type DiagnosticReporter struct {
	readings [][]string
}

func NewDiagnosticReporter(readings []string) DiagnosticReporter {
	return DiagnosticReporter{
		converters.MatrixFromString(
			strings.Join(readings, ""),
			len(readings[0]),
		),
	}
}

func (pm DiagnosticReporter) Diagnose(d Diagnostic) (int64, error) {
	return d(pm)
}

func PowerConsumptionDiagnostic(pm DiagnosticReporter) (int64, error) {
	var gammaBin []string
	var epsilonBin []string
	for i := 0; i < len(pm.readings[0]); i++ {
		sc := counters.NewStringCounter()
		sc.Count(structures.GetColumn(pm.readings, i)...)
		results := sc.Sorted()
		gammaBin = append(gammaBin, results[0])
		epsilonBin = append(epsilonBin, results[1])
	}

	gamma, err := converters.BinaryToInt(gammaBin...)
	if err != nil {
		return 0, err
	}

	epsilon, err := converters.BinaryToInt(epsilonBin...)
	if err != nil {
		return 0, err
	}

	return gamma * epsilon, nil
}

func OxygenGeneratorDiagnostic(pm DiagnosticReporter) (int64, error) {
	readings := pm.readings

	for i := 0; i < len(pm.readings[0]); i++ {
		c := counters.NewStringCounter()
		c.Count(structures.GetColumn(readings, i)...)

		readings = structures.Filter(readings, func(s []string) bool {
			if c.Counts["1"] == c.Counts["0"] {
				return s[i] == "1"
			}

			return s[i] == c.Sorted()[0]
		})

		if len(readings) == 1 {
			break
		}
	}

	return converters.BinaryToInt(readings[0]...)
}

func CO2ScrubberDiagnostic(pm DiagnosticReporter) (int64, error) {
	readings := pm.readings

	for i := 0; i < len(pm.readings[0]); i++ {
		c := counters.NewStringCounter()
		c.Count(structures.GetColumn(readings, i)...)

		readings = structures.Filter(readings, func(s []string) bool {
			if c.Counts["1"] == c.Counts["0"] {
				return s[i] == "0"
			}

			return s[i] == c.Sorted()[1]
		})

		if len(readings) == 1 {
			break
		}
	}

	return converters.BinaryToInt(readings[0]...)
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

	diagnosticReporter := NewDiagnosticReporter(rawBinary)
	rate, err := diagnosticReporter.Diagnose(PowerConsumptionDiagnostic)
	if err != nil {
		return
	}

	log.Printf("Part One: Power Consumption Rate; %d", rate)

	oxygenRating, err := diagnosticReporter.Diagnose(OxygenGeneratorDiagnostic)
	if err != nil {
		return
	}

	co2Rating, err := diagnosticReporter.Diagnose(CO2ScrubberDiagnostic)
	if err != nil {
		return
	}

	log.Printf("Part Two: Life Support Rating; %d", oxygenRating*co2Rating)
}
