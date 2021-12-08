package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

var Reporter = NewDiagnosticReporter(
	[]string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	})

func TestPowerMonitor_PowerRate(t *testing.T) {
	rate, err := Reporter.Diagnose(PowerConsumptionDiagnostic)
	if err != nil {
		assert.FailNow(t, "Failure in Power Monitor test", err)
	}

	assert.Equal(t, int64(198), rate)
}

func TestOxygenGeneratorDiagnostic(t *testing.T) {
	rate, err := Reporter.Diagnose(OxygenGeneratorDiagnostic)
	if err != nil {
		assert.FailNow(t, "Failure in Oxygen Generator test", err)
	}

	assert.Equal(t, int64(23), rate)
}

func TestCO2ScrubberDiagnostic(t *testing.T) {
	rate, err := Reporter.Diagnose(CO2ScrubberDiagnostic)
	if err != nil {
		assert.FailNow(t, "Failure in CO2 Scrubber test", err)
	}

	assert.Equal(t, int64(10), rate)
}
