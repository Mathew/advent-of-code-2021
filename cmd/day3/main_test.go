package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestPowerMonitor_PowerRate(t *testing.T) {
	pm := NewPowerMonitor(
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
	rate, err := pm.PowerRate()
	if err != nil {
		assert.FailNow(t, "Failure in Power Monitor test", err)
	}

	assert.Equal(t, int64(198), rate)
}
