package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestIsHigherNumber(t *testing.T) {
	assert.Equal(t, true, IsHigherNumber(1, 2))
	assert.Equal(t, false, IsHigherNumber(2, 1))
	assert.Equal(t, false, IsHigherNumber(1, 1))
}

func TestCountBoolIf(t *testing.T) {
	counter := CountBoolIf(true)
	assert.Equal(t, 1, counter(true))
	assert.Equal(t, 2, counter(true))
	assert.Equal(t, 2, counter(false))
	assert.Equal(t, 3, counter(true))
}
